import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json 


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["CreateDateScore", "CreateDateProfile", "ResultCode", "AgeProfile", "GraduationYear", "DegreeTypeProfile", "CreditsEarned", "LevelOfEducation", "Salutation", "ComputerAccess", "EmploymentStatus", "Language", "Military", "CampusType", "PlanToStart", "Salary", "SchoolStatus", "TimeToCommit", "UsCitizen", "WorkExperience", "CreditsOutsideUs", "LicensedRn", "LicenseLpn", "TargusEduRollup", "GCU_Preping", "CEC_Preping", "Argosy_PrePing", "UMA_Preping", "UMA_PrePIng_isValid", "State", "Zip"],
                    "Values": [ [ "", "", "value", "0", "0", "value", "0", "0", "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "value", "value", "value", "0", "value", "value", "value", "0" ], [ "", "", "value", "0", "0", "value", "0", "0", "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "value", "value", "value", "0", "value", "value", "value", "0" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/0b3d1614e4ef4060bf0e99ecf0b38f3e/services/9785a56278774f6bbdee7f72692c4d78/execute?api-version=2.0&details=true'
api_key = 'RLcY0t3rUEsEV3mXEgYaBKfQuDVKxFTJ+LGm2O+pltsCj0FLUPCImo5hHHOyOBJeysNS6F0Vr38/gAthSjazgg=='
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 