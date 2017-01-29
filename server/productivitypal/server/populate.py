import datetime


def add_record(user):
    data = {"time_start": datetime.now() - datetime.timedelta(),
            "time_end": datetime.now() - ,
            "time_productive": JSONdict.get("time_productive")}

    user_record = forms.UserRecordForm(data=data).save(commit=False)
    user_record.user_profile = request.user.user_profile
    user_record.save()