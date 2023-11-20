import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facedetectionrealtime-22541-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {

"3130021022":
        {
            "nama": "Mark Zumberk",
            "nim": "3130021022",
            "major": "CEO",
            "tahun_lahir":2000,
            "total_attendance": 10,
            "last_attendance_time": "2023-11-5 19:10:00"
        },
"3130021011":
        {
            "nama": "Rio Rizki",
            "nim": "3130021011",
            "major": "CEO",
            "tahun_lahir":2000,
            "total_attendance": 10,
            "last_attendance_time": "2023-11-5 19:10:00"
        },

"3130021008":
        {
            "nama": "Nanda Dwi Cahyo",
            "nim": "3130021008",
            "major": "CEO",
            "tahun_lahir":2000,
            "total_attendance": 10,
            "last_attendance_time": "2023-11-5 19:10:00"
        },
"3130021021":
        {
            "nama": "Abdur Rochman",
            "nim": "3130021021",
            "major": "Student",
            "tahun_lahir":2002,
            "total_attendance": 10,
            "last_attendance_time": "2023-11-5 19:10:00"
        }
}
for key,value in data.items():
    ref.child(key).set(value)