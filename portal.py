# ============================================================
# 🎓 EDUCATION MANAGEMENT PORTAL
# Complete System - FIXED VERSION
# ============================================================

import os
from datetime import datetime, timedelta

# ============================================================
# COLORS FOR BEAUTIFUL UI
# ============================================================

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    WHITE = '\033[97m'
    MAGENTA = '\033[35m'

# ============================================================
# DATABASE (In-memory storage)
# ============================================================

class Database:
    students = []
    teachers = []
    courses = []
    assignments = []
    attendance_records = []
    exam_records = []
    next_id = 1

# ============================================================
# MODELS
# ============================================================

class Student:
    def __init__(self, name, roll, grade_level, email):
        self.id = Database.next_id
        Database.next_id += 1
        self.name = name
        self.roll = roll
        self.grade_level = grade_level
        self.email = email
        self.grades = {}
        self.attendance = {}
        Database.students.append(self)
    
    def get_avg(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0
    
    def get_weak_subjects(self):
        return [sub for sub, score in self.grades.items() if score < 60]
    
    def get_attendance_percent(self):
        if not self.attendance:
            return 100
        present = sum(1 for v in self.attendance.values() if v)
        return (present / len(self.attendance)) * 100

class Teacher:
    def __init__(self, name, department, email):
        self.id = Database.next_id
        Database.next_id += 1
        self.name = name
        self.department = department
        self.email = email
        Database.teachers.append(self)

class Course:
    def __init__(self, name, code, teacher, schedule):
        self.id = Database.next_id
        Database.next_id += 1
        self.name = name
        self.code = code
        self.teacher = teacher
        self.schedule = schedule
        self.students = []
        Database.courses.append(self)

class Assignment:
    def __init__(self, title, course, due_date, max_score=100):
        self.id = Database.next_id
        Database.next_id += 1
        self.title = title
        self.course = course
        self.due_date = due_date
        self.max_score = max_score
        self.submissions = {}
        Database.assignments.append(self)

class Exam:
    def __init__(self, title, course, date, max_score=100):
        self.id = Database.next_id
        Database.next_id += 1
        self.title = title
        self.course = course
        self.date = date
        self.max_score = max_score
        self.marks = {}
        Database.exam_records.append(self)

# ============================================================
# AI ENGINE
# ============================================================

class AIEngine:
    @staticmethod
    def analyze_student(student):
        avg = student.get_avg()
        weak = student.get_weak_subjects()
        attendance = student.get_attendance_percent()
        
        recommendations = []
        alerts = []
        risk_level = "Low"
        
        # Attendance analysis
        if attendance < 70:
            alerts.append(f"🔴 ATTENDANCE ALERT: {attendance:.1f}%")
            risk_level = "High"
            recommendations.append("📌 Must attend more classes")
        elif attendance < 85:
            recommendations.append("📌 Aim for 85%+ attendance")
        else:
            recommendations.append("✅ Excellent attendance")
        
        # Grade analysis
        if avg < 50:
            alerts.append(f"🔴 GRADE ALERT: {avg:.1f}%")
            risk_level = "High"
            recommendations.append("📚 Immediate academic support needed")
        elif avg < 65:
            recommendations.append("📚 Focus on fundamentals")
            risk_level = "Medium"
        elif avg < 80:
            recommendations.append("📈 Good progress!")
        else:
            recommendations.append("🌟 Excellent performance!")
        
        # Subject analysis
        if weak:
            recommendations.append(f"🎯 Weak subjects: {', '.join(weak)}")
        else:
            recommendations.append("✅ No weak subjects!")
        
        return {
            'average': avg,
            'attendance': attendance,
            'weak_subjects': weak,
            'risk_level': risk_level,
            'recommendations': recommendations,
            'alerts': alerts
        }
    
    @staticmethod
    def analyze_class(students):
        at_risk = []
        top_performers = []
        all_grades = []
        
        for s in students:
            avg = s.get_avg()
            all_grades.append(avg)
            if avg < 60:
                at_risk.append((s.name, avg))
            elif avg >= 80:
                top_performers.append((s.name, avg))
        
        return {
            'class_avg': sum(all_grades) / len(all_grades) if all_grades else 0,
            'at_risk': at_risk,
            'top_performers': top_performers,
            'total': len(students)
        }

# ============================================================
# DISPLAY FUNCTIONS
# ============================================================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(f"""
{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║   {Colors.BOLD}🎓  EDUCATION MANAGEMENT PORTAL  🎓{Colors.END}{Colors.CYAN}                                    ║
║   {Colors.BOLD}🤖  AI-Powered Academic Intelligence{Colors.END}{Colors.CYAN}                                    ║
║                                                                            ║
║   {Colors.WHITE}📅 {datetime.now().strftime('%B %d, %Y  |  %I:%M %p')}{Colors.END}{Colors.CYAN}                          ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝{Colors.END}
""")

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}┌{'─' * 56}┐{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}│ {text.center(54)} │{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}└{'─' * 56}┘{Colors.END}\n")

# ============================================================
# SAMPLE DATA
# ============================================================

def create_sample_data():
    # Teachers
    t1 = Teacher("Prof. Sharma", "Mathematics", "sharma@edu.com")
    t2 = Teacher("Prof. Gupta", "Science", "gupta@edu.com")
    t3 = Teacher("Prof. Patel", "English", "patel@edu.com")
    
    # Courses
    c1 = Course("Mathematics 101", "MATH101", t1, "Mon/Wed 10:00")
    c2 = Course("Physics 101", "PHY101", t2, "Tue/Thu 10:00")
    c3 = Course("English 101", "ENG101", t3, "Mon/Wed 1:00")
    c4 = Course("Chemistry 101", "CHEM101", t2, "Tue/Thu 1:00")
    
    # Students with grades
    s1 = Student("Rahul Kumar", "S001", "10th", "rahul@edu.com")
    s1.grades = {c1.id: 88, c2.id: 85, c3.id: 90, c4.id: 82}
    s1.attendance = {'2026-08-01': True, '2026-08-02': True, '2026-08-03': True, '2026-08-04': False, '2026-08-05': True}
    
    s2 = Student("Priya Sharma", "S002", "10th", "priya@edu.com")
    s2.grades = {c1.id: 72, c2.id: 68, c3.id: 75, c4.id: 70}
    s2.attendance = {'2026-08-01': True, '2026-08-02': True, '2026-08-03': False, '2026-08-04': True, '2026-08-05': True}
    
    s3 = Student("Amit Singh", "S003", "10th", "amit@edu.com")
    s3.grades = {c1.id: 45, c2.id: 50, c3.id: 55, c4.id: 48}
    s3.attendance = {'2026-08-01': False, '2026-08-02': False, '2026-08-03': True, '2026-08-04': False, '2026-08-05': False}
    
    s4 = Student("Sneha Patel", "S004", "10th", "sneha@edu.com")
    s4.grades = {c1.id: 82, c2.id: 79, c3.id: 85, c4.id: 90}
    s4.attendance = {'2026-08-01': True, '2026-08-02': True, '2026-08-03': True, '2026-08-04': True, '2026-08-05': True}
    
    s5 = Student("Vikram Raj", "S005", "10th", "vikram@edu.com")
    s5.grades = {c1.id: 58, c2.id: 62, c3.id: 65, c4.id: 60}
    s5.attendance = {'2026-08-01': True, '2026-08-02': False, '2026-08-03': True, '2026-08-04': True, '2026-08-05': False}
    
    # Enroll students in courses
    for course in Database.courses:
        course.students = [s.id for s in Database.students]
    
    # Assignments
    Assignment("Math Quiz 1", c1, "2026-08-20", 50)
    Assignment("Physics Lab", c2, "2026-08-25", 100)
    Assignment("English Essay", c3, "2026-08-22", 75)
    Assignment("Chemistry Lab", c4, "2026-08-28", 100)
    
    # Exams
    Exam("Math Mid-Term", c1, "2026-09-01", 100)
    Exam("Physics Mid-Term", c2, "2026-09-05", 100)
    Exam("English Mid-Term", c3, "2026-09-03", 100)

# ============================================================
# DASHBOARDS
# ============================================================

def student_dashboard():
    clear()
    print_banner()
    print_header("👨‍🎓  STUDENT DASHBOARD")
    
    print(f"{Colors.WHITE}📋 Select a student:{Colors.END}\n")
    for i, s in enumerate(Database.students, 1):
        avg = s.get_avg()
        status = f"{Colors.GREEN}✅{Colors.END}" if avg >= 70 else f"{Colors.YELLOW}⚠️{Colors.END}" if avg >= 60 else f"{Colors.RED}❌{Colors.END}"
        print(f"  {Colors.BOLD}{i}.{Colors.END} {s.name} - Avg: {avg:.1f}% {status}")
    
    try:
        choice = int(input(f"\n{Colors.CYAN}👉 Enter number: {Colors.END}")) - 1
        if 0 <= choice < len(Database.students):
            student = Database.students[choice]
            ai = AIEngine.analyze_student(student)
            
            clear()
            print_banner()
            print_header(f"👋  {student.name}'s Report")
            
            print(f"{Colors.WHITE}📋 Roll: {Colors.CYAN}{student.roll}{Colors.END}")
            print(f"{Colors.WHITE}📚 Grade: {Colors.CYAN}{student.grade_level}{Colors.END}")
            print(f"{Colors.WHITE}📊 Average: {Colors.BOLD}{Colors.GREEN if student.get_avg() >= 70 else Colors.YELLOW}{student.get_avg():.1f}%{Colors.END}")
            print(f"{Colors.WHITE}📅 Attendance: {Colors.BOLD}{Colors.GREEN if student.get_attendance_percent() >= 85 else Colors.YELLOW}{student.get_attendance_percent():.1f}%{Colors.END}")
            
            # Grades
            print(f"\n{Colors.BOLD}📚 GRADES{Colors.END}")
            print(f"{Colors.CYAN}┌{'─' * 40}┐{Colors.END}")
            for course_id, score in student.grades.items():
                course = next((c for c in Database.courses if c.id == course_id), None)
                if course:
                    status = f"{Colors.GREEN}✅{Colors.END}" if score >= 70 else f"{Colors.YELLOW}⚠️{Colors.END}" if score >= 60 else f"{Colors.RED}❌{Colors.END}"
                    bar = f"{Colors.GREEN}{'█' * int(score/10)}{Colors.END}{Colors.WHITE}{'░' * (10 - int(score/10))}{Colors.END}"
                    print(f"│ {course.name:<15} {score:>3}% {status}  {bar} │")
            print(f"{Colors.CYAN}└{'─' * 40}┘{Colors.END}")
            
            # AI Recommendations
            print(f"\n{Colors.BOLD}{Colors.MAGENTA}🤖 AI RECOMMENDATIONS{Colors.END}")
            print(f"{Colors.CYAN}┌{'─' * 54}┐{Colors.END}")
            print(f"│ {Colors.WHITE}Risk Level: {Colors.RED if ai['risk_level'] == 'High' else Colors.YELLOW if ai['risk_level'] == 'Medium' else Colors.GREEN}{ai['risk_level']}{Colors.END}".ljust(56) + "│")
            for rec in ai['recommendations']:
                print(f"│ {rec:<52} │")
            print(f"{Colors.CYAN}└{'─' * 54}┘{Colors.END}")
    except:
        print(f"{Colors.RED}❌ Invalid input!{Colors.END}")
    
    input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")

def teacher_dashboard():
    clear()
    print_banner()
    print_header("👨‍🏫  TEACHER DASHBOARD")
    
    # Show teachers
    for i, t in enumerate(Database.teachers, 1):
        print(f"  {i}. {t.name} - {t.department}")
    
    try:
        choice = int(input(f"\n{Colors.CYAN}👉 Select teacher: {Colors.END}")) - 1
        if 0 <= choice < len(Database.teachers):
            teacher = Database.teachers[choice]
            
            # Get teacher's courses
            courses = [c for c in Database.courses if c.teacher == teacher]
            
            print(f"\n{Colors.WHITE}👤 Teacher: {Colors.CYAN}{teacher.name}{Colors.END}")
            print(f"{Colors.WHITE}📚 Courses: {Colors.CYAN}{len(courses)}{Colors.END}")
            
            # Class analysis
            analysis = AIEngine.analyze_class(Database.students)
            
            print(f"\n{Colors.BOLD}📊 CLASS PERFORMANCE{Colors.END}")
            print(f"{Colors.CYAN}┌{'─' * 50}┐{Colors.END}")
            print(f"│ {Colors.WHITE}Total Students:{Colors.END} {Colors.CYAN}{analysis['total']}{Colors.END}".ljust(52) + "│")
            print(f"│ {Colors.WHITE}Class Average:{Colors.END} {Colors.CYAN}{analysis['class_avg']:.1f}%{Colors.END}".ljust(52) + "│")
            print(f"│ {Colors.WHITE}At-Risk:{Colors.END} {Colors.RED}{len(analysis['at_risk'])}{Colors.END}".ljust(52) + "│")
            print(f"│ {Colors.WHITE}Top Performers:{Colors.END} {Colors.GREEN}{len(analysis['top_performers'])}{Colors.END}".ljust(52) + "│")
            print(f"{Colors.CYAN}└{'─' * 50}┘{Colors.END}")
            
            # AI Insights
            print(f"\n{Colors.BOLD}{Colors.MAGENTA}🤖 AI INSIGHTS{Colors.END}")
            print(f"{Colors.CYAN}┌{'─' * 54}┐{Colors.END}")
            if analysis['at_risk']:
                print(f"│ {Colors.RED}⚠️ At-Risk Students:{Colors.END}".ljust(56) + "│")
                for name, avg in analysis['at_risk']:
                    print(f"│   {Colors.YELLOW}• {name}: {avg:.1f}%{Colors.END}".ljust(56) + "│")
            else:
                print(f"│ {Colors.GREEN}✅ No at-risk students!{Colors.END}".ljust(56) + "│")
            print(f"{Colors.CYAN}└{'─' * 54}┘{Colors.END}")
    except:
        print(f"{Colors.RED}❌ Invalid input!{Colors.END}")
    
    input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")

def admin_dashboard():
    clear()
    print_banner()
    print_header("🏛️  ADMIN DASHBOARD")
    
    analysis = AIEngine.analyze_class(Database.students)
    
    print(f"{Colors.BOLD}📊 SYSTEM STATISTICS{Colors.END}")
    print(f"{Colors.CYAN}┌{'─' * 50}┐{Colors.END}")
    print(f"│ {Colors.WHITE}Total Students:{Colors.END} {Colors.CYAN}{len(Database.students)}{Colors.END}".ljust(52) + "│")
    print(f"│ {Colors.WHITE}Total Teachers:{Colors.END} {Colors.CYAN}{len(Database.teachers)}{Colors.END}".ljust(52) + "│")
    print(f"│ {Colors.WHITE}Total Courses:{Colors.END} {Colors.CYAN}{len(Database.courses)}{Colors.END}".ljust(52) + "│")
    print(f"│ {Colors.WHITE}Total Assignments:{Colors.END} {Colors.CYAN}{len(Database.assignments)}{Colors.END}".ljust(52) + "│")
    print(f"│ {Colors.WHITE}Total Exams:{Colors.END} {Colors.CYAN}{len(Database.exam_records)}{Colors.END}".ljust(52) + "│")
    print(f"│ {Colors.WHITE}Class Average:{Colors.END} {Colors.CYAN}{analysis['class_avg']:.1f}%{Colors.END}".ljust(52) + "│")
    print(f"│ {Colors.WHITE}At-Risk Students:{Colors.END} {Colors.RED}{len(analysis['at_risk'])}{Colors.END}".ljust(52) + "│")
    print(f"{Colors.CYAN}└{'─' * 50}┘{Colors.END}")
    
    # Subject analysis
    print(f"\n{Colors.BOLD}📚 SUBJECT ANALYSIS{Colors.END}")
    print(f"{Colors.CYAN}┌{'─' * 50}┐{Colors.END}")
    subjects = ['Math', 'Science', 'English', 'Chemistry']
    for subject in subjects:
        scores = []
        for s in Database.students:
            for c_id, grade in s.grades.items():
                course = next((c for c in Database.courses if c.id == c_id), None)
                if course and subject in course.name:
                    scores.append(grade)
        if scores:
            avg = sum(scores) / len(scores)
            status = f"{Colors.GREEN}✅ Good{Colors.END}" if avg >= 70 else f"{Colors.YELLOW}⚠️ Avg{Colors.END}" if avg >= 60 else f"{Colors.RED}❌ Poor{Colors.END}"
            print(f"│ {subject:<15} {avg:>6.1f}%  {status:<10} │")
    print(f"{Colors.CYAN}└{'─' * 50}┘{Colors.END}")
    
    input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")

def view_courses():
    clear()
    print_banner()
    print_header("📚  COURSES")
    
    for c in Database.courses:
        print(f"\n{Colors.BOLD}{Colors.CYAN}📖 {c.name}{Colors.END}")
        print(f"  Code: {c.code}")
        print(f"  Teacher: {c.teacher.name}")
        print(f"  Schedule: {c.schedule}")
        print(f"  Students: {len(c.students)}")
    
    input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")

# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:
        clear()
        print_banner()
        print(f"""
{Colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}

  {Colors.BOLD}📌  MAIN MENU{Colors.END}

  {Colors.GREEN}1.{Colors.END} 👨‍🎓  {Colors.WHITE}Student Dashboard{Colors.END}
  {Colors.YELLOW}2.{Colors.END} 👨‍🏫  {Colors.WHITE}Teacher Dashboard{Colors.END}
  {Colors.MAGENTA}3.{Colors.END} 🏛️   {Colors.WHITE}Admin Dashboard{Colors.END}
  {Colors.BLUE}4.{Colors.END} 📚   {Colors.WHITE}View All Courses{Colors.END}
  {Colors.RED}5.{Colors.END} 🚪   {Colors.WHITE}Exit{Colors.END}

{Colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}
""")
        
        choice = input(f"{Colors.CYAN}👉 Enter your choice (1-5): {Colors.END}")
        
        if choice == '1':
            student_dashboard()
        elif choice == '2':
            teacher_dashboard()
        elif choice == '3':
            admin_dashboard()
        elif choice == '4':
            view_courses()
        elif choice == '5':
            clear()
            print(f"""
{Colors.GREEN}╔══════════════════════════════════════════════════════════════╗
║                                                                  ║
║   {Colors.BOLD}🎓  Thank you for using the AI Education Portal!  🎓{Colors.END}{Colors.GREEN}   ║
║   {Colors.WHITE}📚  Keep learning and growing!{Colors.END}{Colors.GREEN}                            ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝{Colors.END}
""")
            break
        else:
            print(f"{Colors.RED}❌ Invalid choice!{Colors.END}")
            input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    print(f"{Colors.CYAN}📦 Creating sample data...{Colors.END}")
    create_sample_data()
    print(f"{Colors.GREEN}✅ System ready!{Colors.END}")
    input(f"{Colors.CYAN}Press Enter to start...{Colors.END}")
    main()
