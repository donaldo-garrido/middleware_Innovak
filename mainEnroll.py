from .enrollmentsPerson_SabaAPI import enrollmentsPerson_SABA
from .detailsEnroll import detailsEnroll_SABA
from .userEnrollment_CrehanaAPI import userEnrollment_CREHANA


enrollements = enrollmentsPerson_SABA()

for iDs, enrolls in enrollements:
    for id_enroll in enrolls:
        class_name = detailsEnroll_SABA(id_enroll)

        if class_name != False:
            
