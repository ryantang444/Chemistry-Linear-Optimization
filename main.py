import pulp
import csv
import pandas as pd




def read_entire_school_year(filename):
   
    fields = ["Semester" , "Academic Year" , "Course ID Number" , "Subject" , "Course Number" , "Section" , "Course Type", "Enrollment as of Add Date", "# majored in STEM", "Days", "Start Time" , "End Time" , "Enrollment End of Term", "Enrollment as of Census"]


    rows = []
    #read the file
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)


    # extracting field names through first row
        fields = next(csvreader)


    # extracting each data row one by one
        for row in csvreader:
            rows.append(row)


        print("Total no. of rows: %d" % (csvreader.line_num))


    print('Field names are:' + ', '.join(field for field in fields))


    print('Spring 2020')
    for row in rows:
        # parsing each column of a row
        for col in row:
            print("%10s" % col, end=" "),
        print('\n')




def group_scheduling_info(filename):
    df = pd.read_csv(filename)


    #Group for Days, start and end time
    scheduling_info = df.groupby(["Days", "Start Time", "End Time"])


    result_scheduling_info = scheduling_info.sum()


    print(result_scheduling_info)


def group_course_info(filename):
    df = pd.read_csv(filename)
    #Group for class Course ID Number,Subject ,Course Number,Section,Course Type
    course_info = df.groupby(["Course ID Number", "Subject ", "Course Number", "Section", "Course Type"])


    result_course_info = course_info.sum()


    print(result_course_info)


print("\n Showing co enrollment data")


def get_co_enrollment_data(filename):
    #Co-enrollment data
    co_enrollment_df = pd.read_csv("spring co enrollment.csv")


    print(co_enrollment_df)


    co_enrollment_df = pd.read_csv("spring co enrollment.csv")




def extract_co_enrollment_pairs(filename):
  """Extracts course pairs from a CSV file.
  Returns:
    A list of tuples, where each tuple represents a course pair.
  """


  course_pairs = []
  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row


    for row in csvreader:
      course1, course2, *_ = row
      course_pairs.append((course1, course2))


  return course_pairs





def extract_time_slots(filename):
    df = pd.read_csv(filename)
    df['Time Slot'] = df['Days'] + ' ' + df['Start Time'] + '-' + df['End Time']
    time_slots = df['Time Slot'].unique()
    return time_slots

def get_coenrollment_count(course1, course2, term, co_enrollment_file):
  """Retrieves the co-enrollment count for a given course pair and term.
  Returns:
    The co-enrollment count for the given course pair and term, or 0 if not found.
  """


  if (course1, course2, term) in co_enrollment_file:
    return co_enrollment_file[(course1, course2, term)]
  elif (course2, course1, term) in co_enrollment_file:
    return co_enrollment_file[(course2, course1, term)]
  else:
    return 0
 
def analyze_overlaps(pairs, overlap_dict, term):
  """Analyzes overlaps between course pairs based on co-enrollment counts.
  Returns:
    A list of tuples containing course pairs and their total co-enrollment count for Spring 2023.
  """
  overlaps = []
  for course1, course2 in pairs:
    total_overlap = get_coenrollment_count(course1, course2, "Spring 2023", overlap_dict)
    print(total_overlap)
    overlaps.append(((course1, course2), total_overlap))


  return overlaps


# Create a dictionary for co-enrollment overlap
def get_overlap(filename, term='Spring 2023'):
    #Creates a dictionary for co-enrollment overlaps for a specific term.
    overlap = {}
    term_index = {'Spring 2023': 1, 'Spring 2022': 2, 'Spring 2020': 3}  # Map term to column index
    
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row

        for row in csvreader:
            if row[0] == "Combination:":
                continue  # Skip the second header row if present
            
            course1, course2 = row[0].strip(), row[1].strip()
            coenrollment_count = int(row[term_index[term]])  # Get the co-enrollment count for the specified term
            
            pair = (course1, course2)
            overlap[pair] = coenrollment_count
    
    return overlap

filename_spring_2023 = "spring 2023.csv"
filename_co_enrollment = "spring co enrollment.csv"
pairs = extract_co_enrollment_pairs(filename_co_enrollment)

# Define the course pairs and the overlap dictionary
filename_co_enrollment = "spring co enrollment.csv"
overlap_dict = get_overlap(filename_co_enrollment, term='Spring 2022')

# List of courses (extract them from the dictionary keys)
courses = list(set([course for pair in overlap_dict.keys() for course in pair]))
print("\n overlap dict", overlap_dict)

# Time slots for scheduling
time_slots_file = extract_time_slots(filename_spring_2023)
time_slots_array = []
for time in time_slots_file:
  time_slots_array.append(time)
print(time_slots_array)

#time_slots = [1, 2, 3, 4, 5, 6]

# Initialize the problem
prob = pulp.LpProblem("Course_Scheduling", pulp.LpMinimize)

# Define variables
x = pulp.LpVariable.dicts("x", ((c, t) for c in courses for t in time_slots_array), cat='Binary')

# Define auxiliary variables to capture overlap in the same time slot
z = pulp.LpVariable.dicts("z", overlap_dict.keys(), lowBound=0, cat='Continuous')

# Objective function: minimize overlaps in the same time slot
prob += pulp.lpSum(overlap_dict[(c1, c2)] * z[(c1, c2)] for (c1, c2) in overlap_dict)

# Constraints: Each course is scheduled exactly once
for c in courses:
    prob += pulp.lpSum(x[c, t] for t in time_slots_array) == 1

# Constraints: Capture overlap in the same time slot
for (c1, c2) in overlap_dict:
    for t in time_slots_array:
        prob += z[(c1, c2)] >= x[c1, t] + x[c2, t] - 1

# Solve the problem
prob.solve()

# Output the results
for t in time_slots_array:
    scheduled_courses = [c for c in courses if pulp.value(x[c, t]) == 1]
    print(f"Courses {', '.join(scheduled_courses)} are scheduled for time slot {t}")