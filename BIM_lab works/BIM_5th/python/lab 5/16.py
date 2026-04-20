class Time:
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute

    def add_time(self, t1, t2):
        total_min = t1.minute + t2.minute
        extra_hour = total_min // 60
        final_minute = total_min % 60
        total_hours = t1.hour + t2.hour + extra_hour
        return Time(total_hours, final_minute)

    def display(self):
        print(f"{self.hour} hour(s) {self.minute} minute(s)")


t1 = Time(2, 50)
t2 = Time(3, 20)
t3 = Time()

t3 = t3.add_time(t1, t2)

print("Result Time:")
t3.display()