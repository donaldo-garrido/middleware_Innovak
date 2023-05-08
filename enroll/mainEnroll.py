from enrollmentsPerson_SabaAPI import enrollmentsPerson_SABA
from detailsEnroll_SabaAPI import detailsEnroll_SABA
from userEnrollment_CrehanaAPI import userEnrollment_CREHANA

counter = 0
enrollments = enrollmentsPerson_SABA()

print(type(enrollments))
print(len(enrollments))

print('--------------------------------')

for usr in enrollments:
    lst_enrolls = enrollments[usr]
    #print(usr)
    #print(lst_enrolls)

   
    user_id = '224861'

    for id_enroll in lst_enrolls:
        #print(id_enroll)
        class_name = detailsEnroll_SABA(id_enroll)

        if class_name != False and counter<1:
            
            #9491, 11161
            class_id = '11161'
            content, statusStatement = userEnrollment_CREHANA(user_id, class_id)

            print('--------------------------------------')
            print(statusStatement)
            print(content)
            print('--------------------------------------')
            counter+=1