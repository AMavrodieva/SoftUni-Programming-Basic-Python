workdays = int(input())
earned_money_per_day = float(input())
course_usd_bgn = float(input())
month_income = workdays * earned_money_per_day
yearly_ner_salary = (12 * month_income + 2.5 * month_income) * 0.75
print("%.2f" % (yearly_ner_salary / 365 * course_usd_bgn))