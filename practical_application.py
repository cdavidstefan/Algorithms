# The ability to efficiently and accurately search data in a given data repository is critical to
# many real-life applications. Depending on your choice of searching algorithm, you may
# need to sort the data first as well. The choice of the right sorting and searching algorithms
# will depend on the type and the size of the data, as well as the nature of the problem you
# are trying to solve.
# Let's try to use the algorithms presented in this chapter to solve the problem of matching a
# new applicant at the immigration department of a certain country with historical records.
# When someone applies for a visa to enter the country, the system tries to match the
# applicant with the existing historical records. If at least one match is found, then the system
# further calculates the number of times that the individual has been approved or refused in
# the past. On the other hand, if no match is found, the system classes the applicant as a new
# applicant and issues them a new identifier. The ability to search, locate, and identify a
# person in the historical data is critical for the system. This information is important because
# if someone has applied in the past and the application is known to have been refused, then
# this may affect that individual's current application in a negative way. Similarly, if
# someone's application is known to have been approved in the past, this approval may
# increase the chances of that individual getting approval for their current application.
# Typically, the historical database will have millions of rows, and we will need a well designed
# solution to match new applicants in the historical database.

# Let's assume that the historical table in the database looks like the following:
#
    # Personal ID   Application ID First name Surname     DOB      Decision   Decision date
    # 45583         677862         John       Doe     2000-09-19  Approved   2018-08-07
    # 54543         877653        Xman       Xsir    1970-03-10  Rejected   2018-06-07
    # 34332         344565        Agro       Waka    1973-02-15  Rejected   2018-05-05
    # 45583         677864        John       Doe     2000-09-19  Approved   2018-03-02
    # 22331         344553        Kal        Sorts   1975-01-02  Approved   2018-04-15
#
# In this table, the first column, Personal ID, is associated with each of the unique
# applicants in the historical database. If there are 30 million unique applicants in the
# historical database, then there will be 30 million unique personal IDs. Each personal ID
# identifies an applicant in the historical database system.
# The second column we have is Application ID. Each application ID identifies a unique
# application in the system. A person may have applied more than once in the past. So, this
# means that in the historical database, we will have more unique application IDs than
# personal IDs. John Doe will only have one personal ID but has two application IDs, as
# shown in the preceding table.

# The preceding table only shows a sample of the historical dataset. Let's assume that we
# have close to 1 million rows in our historical dataset, which contains the records of the last
# 10 years of applicants. New applicants are continuously arriving at the average rate of
# around 2 applicants per minute. For each applicant, we need to do the following:


# 1. Issue a new application ID for the applicant

# This module provides immutable UUID objects (universally unique identifiers)
import uuid

# Definin clasa Applicant cu proprietatile din tabel. Cand vrem sa adaugam in tabel
# Facem o noua instanta a clasei.
class Applicant:
    def __init__(self, personal_id, first_name, surname, dob, decision, decision_date):
        self.personal_id = personal_id
        self.application_id = None
        self.first_name = first_name
        self.surname = surname
        self.dob = dob
        self.decision = decision
        self.decision_date = decision_date

    def is_match(self, other_applicant):
        return (
            self.personal_id == other_applicant.personal_id
        )

# Lista de aplicanti reprezinta intrarile anterioare din tabel.

historical_applicants = [
    Applicant(personal_id=45583, first_name='John', surname='Doe', dob='2000-09-19', decision='Approved', decision_date='2018-08-07'),
    Applicant(personal_id=54543, first_name='Xman', surname='Xsir', dob='1970-03-10', decision='Rejected', decision_date='2018-06-07'),
    # ... more entries
]


table_row = {'Personal ID': 000000, 'First name': 'John', 'Surname': 'Doe', 'DOB': '2000-09-19', 'Decision': 'Pending', 'Decision date': '2024-02-02'}
# Pe baza cererii completate (table_row) creăm o nouă instanță a clasei Applicant:

new_applicant = Applicant(
    personal_id=table_row['Personal ID'],
    first_name=table_row['First name'],
    surname=table_row['Surname'],
    dob=table_row['DOB'],
    decision=table_row['Decision'],
    decision_date=table_row['Decision date']
)

# Checking for a match in the historical applicants table
matching_applicant = None
for existing_applicant in historical_applicants:
    if new_applicant.is_match(existing_applicant):
        matching_applicant = existing_applicant
        break

if matching_applicant:
    print(f"Match found in the historical database. Personal ID: {matching_applicant.personal_id}")

    # Counting the number of approvals and refusals
    approval_count = sum(1 for applicant in historical_applicants if applicant.personal_id == matching_applicant.personal_id and applicant.decision == 'Approved')
    refusal_count = sum(1 for applicant in historical_applicants if applicant.personal_id == matching_applicant.personal_id and applicant.decision == 'Rejected')

    print(f"Number of approvals: {approval_count}")
    print(f"Number of refusals: {refusal_count}")
else:
    # If no match is found, issue a new personal ID
    new_personal_id = str(uuid.uuid4())
    print(f"No match found. Issuing a new Personal ID: {new_personal_id}")






# Sort the historical database by dob:
# Because we have a large dataset we must use an algorithm
# with low time complexity. Merge Sort will do

def merge_sort(applicants, key='dob'):
    if len(applicants) <= 1:
        return  applicants

    mid = len(applicants) // 2
    left = merge_sort(applicants[:mid], key=key)
    right = merge_sort(applicants[mid:], key=key)

    return merge(left, right, key=key)

def merge(left, right, key='dob'):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        left_key_value = left[i].dob if key == 'dob' else getattr(left[i], key)
        right_key_value = right[j].dob if key == 'dob' else getattr(right[j], key)

        if left_key_value < right_key_value:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

sorted_historical_applicants = merge_sort(historical_applicants, key='dob')