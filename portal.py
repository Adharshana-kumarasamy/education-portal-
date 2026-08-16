# ============================================
# 🎓 COMPLETE EDUCATION MANAGEMENT PORTAL
# AI-Powered Academic Intelligence
# ============================================

import os

# ============================================
# STUDENT CLASS
# ============================================

class Student:
    def __init__(self, name, roll, grades):
        self.name = name
        self.roll = roll
        self.grades = grades
    
    def get_avg(self):
        return sum(self.grades.values()) / len(self.grades)
    
    def get_weak_subjects(self):
        weak = []
        for subject, score in self.grades.items():
            if score < 60:
                weak.append(subject)
        return weak
    
    def get_strong_subjects(self):
        strong = []
        for subject, score in self.grades.items():
            if score >= 80:
                strong.append(subject)
        return strong

# ============================================
# SAMPLE STUDENTS
# ============================================

students = [
    Student("Rahul Kumar", "S001", {'Math': 88, 'Science': 85, 'English': 90, 'History': 82}),
    Student("Priya Sharma", "S002", {'Math': 72, 'Science': 68, 'English': 75, 'History': 70}),
    Student("Amit Singh", "S003", {'Math': 45, 'Science': 50, 'English': 55, 'History': 48}),
    Student("Sneha Patel", "S004", {'Math': 82, 'Science': 79, 'English': 85, 'History': 90}),
    Student("Vikram Raj", "S005", {'Math': 58, 'Science': 62, 'English': 65, 'History': 60}),
]

# ============================================
# TEACHER CLASS
# ============================================

class Teacher:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    
    def get_class_performance(self):
        all_grades = []
        for s in students:
            all_grades.extend(s.grades.values())
        return sum(all_grades) / len(all_grades) if all_grades else 0

teachers = [
    Teacher("Prof. Sharma", "Mathematics"),
    Teacher("Prof. Gupta", "Science"),
]

# ============================================
# AI INTELLIGENCE ENGINE
# ============================================

def get_ai_recommendations(student):
    """Generate personalized AI recommendations for a student"""
    recommendations = []
    avg = student.get_avg()
    weak = student.get_weak_subjects()
    strong = student.get_strong_subjects()
    
    # Performance analysis
    if avg < 50:
        recommendations.append("🔴 CRITICAL: Your average is below 50%!")
        recommendations.append("📚 You need immediate academic support")
    elif avg < 65:
        recommendations.append("📚 Your grades need improvement")
        recommendations.append("📖 Study 2 extra hours daily on weak subjects")
    elif avg < 80:
        recommendations.append("📈 Good progress! Keep practicing")
        recommendations.append("🎯 Aim for 80%+ in your next exams")
    else:
        recommendations.append("🌟 EXCELLENT! You're a top performer!")
        recommendations.append("🏆 Keep up the great work!")
    
    # Subject analysis
    if weak:
        recommendations.append(f"🎯 Weak subjects: {', '.join(weak)}")
        recommendations.append(f"📖 Focus extra time on: {', '.join(weak)}")
    else:
        recommendations.append("✅ No weak subjects detected!")
    
    if strong:
        recommendations.append(f"💪 Strong subjects: {', '.join(strong)}")
    
    # Personalized tip
    if len(weak) >= 2:
        recommendations.append("💡 Create a study schedule prioritizing weak subjects")
    elif avg >= 85 and len(weak) == 0:
        recommendations.append("🎓 You're ready for advanced topics!")
    
    return recommendations

# ============================================
# DISPLAY FUNCTIONS
# ============================================

def display_header():
    print("\n" + "="*60)
    print("  🎓  EDUCATION MANAGEMENT PORTAL  🎓")
    print("  AI-Powered Academic Intelligence")
    print("="*60)

def student_dashboard():
    """Student Dashboard with AI Insights"""
    print("\n" + "="*60)
    print("  👨‍🎓  STUDENT DASHBOARD")
    print("="*60)
    
    # Show all students
    print("\n📋 Select a student:")
    for i, s in enumerate(students, 1):
        avg = s.get_avg()
        status = "✅" if avg >= 70 else "⚠️" if avg >= 60 else "❌"
        print(f"  {i}. {s.name} - Avg: {avg:.1f}% {status}")
    
    try:
        choice = int(input("\nEnter student number (1-5): ")) - 1
        if 0 <= choice < len(students):
            s = students[choice]
            ai = get_ai_recommendations(s)
            
            # Student info
            print(f"\n👋 Welcome, {s.name}")
            print(f"📋 Roll Number: {s.roll}")
            print(f"📊 Average Grade: {s.get_avg():.1f}%")
            
            # Grades
            print("\n📚 GRADES:")
            print("-"*30)
            for subject, score in s.grades.items():
                status = "✅" if score >= 70 else "⚠️" if score >= 60 else "❌"
                print(f"  {subject:10}: {score:3}%  {status}")
            
            # AI Recommendations
            print("\n" + "="*50)
            print("  🤖  AI RECOMMENDATIONS")
            print("="*50)
            for rec in ai:
                print(f"  {rec}")
            print("="*50)
        else:
            print("❌ Invalid selection!")
    except:
        print("❌ Invalid input!")

def teacher_dashboard():
    """Teacher Dashboard with Class Analytics"""
    print("\n" + "="*60)
    print("  👨‍🏫  TEACHER DASHBOARD")
    print("="*60)
    
    # Teacher info
    t = teachers[0]
    print(f"\n👤 Teacher: {t.name}")
    print(f"📚 Department: {t.department}")
    
    # Class performance
    print("\n📊 CLASS PERFORMANCE:")
    print("-"*30)
    
    total_students = len(students)
    all_grades = []
    for s in students:
        all_grades.extend(s.grades.values())
    class_avg = sum(all_grades) / len(all_grades) if all_grades else 0
    
    print(f"  Total Students: {total_students}")
    print(f"  Class Average: {class_avg:.1f}%")
    
    # Student list with performance
    print("\n👨‍🎓 STUDENT PERFORMANCE:")
    print("-"*40)
    for s in students:
        avg = s.get_avg()
        status = "✅" if avg >= 70 else "⚠️" if avg >= 60 else "❌"
        weak = s.get_weak_subjects()
        weak_text = f" (Weak: {', '.join(weak)})" if weak else " ✅ All good!"
        print(f"  {s.name:15} {avg:6.1f}%  {status}{weak_text}")
    
    # AI Insights for Teacher
    print("\n" + "="*50)
    print("  🤖  AI INSIGHTS FOR TEACHER")
    print("="*50)
    
    at_risk = [s for s in students if s.get_avg() < 60]
    high_performers = [s for s in students if s.get_avg() >= 80]
    
    if at_risk:
        print(f"  ⚠️ At-Risk Students ({len(at_risk)}):")
        for s in at_risk:
            print(f"     - {s.name}: {s.get_avg():.1f}%")
        print("  📌 Schedule extra help sessions for at-risk students")
    else:
        print("  ✅ No at-risk students!")
    
    if high_performers:
        print(f"  🌟 Top Performers ({len(high_performers)}):")
        for s in high_performers:
            print(f"     - {s.name}: {s.get_avg():.1f}%")
    
    print("="*50)

def admin_dashboard():
    """Admin Dashboard with System Analytics"""
    print("\n" + "="*60)
    print("  🏛️  ADMIN DASHBOARD")
    print("="*60)
    
    # System statistics
    print("\n📊 SYSTEM STATISTICS:")
    print("-"*30)
    print(f"  Total Students: {len(students)}")
    print(f"  Total Teachers: {len(teachers)}")
    
    # Performance overview
    all_grades = []
    for s in students:
        all_grades.extend(s.grades.values())
    
    if all_grades:
        overall_avg = sum(all_grades) / len(all_grades)
        print(f"  Overall Average: {overall_avg:.1f}%")
    
    # At-risk students
    at_risk = [s for s in students if s.get_avg() < 60]
    print(f"  At-Risk Students: {len(at_risk)}")
    
    # Subject analysis
    print("\n📚 SUBJECT ANALYSIS:")
    print("-"*30)
    subjects = ['Math', 'Science', 'English', 'History']
    for subject in subjects:
        scores = [s.grades.get(subject, 0) for s in students]
        avg = sum(scores) / len(scores) if scores else 0
        status = "✅" if avg >= 70 else "⚠️" if avg >= 60 else "❌"
        print(f"  {subject:10}: {avg:.1f}%  {status}")
    
    # AI Summary
    print("\n" + "="*50)
    print("  🤖  AI SYSTEM SUMMARY")
    print("="*50)
    
    if at_risk:
        print(f"  ⚠️ {len(at_risk)} students need academic support:")
        for s in at_risk:
            weak = s.get_weak_subjects()
            print(f"     - {s.name}: Weak in {', '.join(weak)}")
    else:
        print("  ✅ All students are performing well!")
    
    print("  📌 AI recommends:")
    if at_risk:
        print("     - Provide extra tutoring for at-risk students")
    if len([s for s in students if s.get_avg() >= 80]) >= 3:
        print("     - Consider advanced programs for top performers")
    print("="*50)

# ============================================
# MAIN MENU
# ============================================

def main():
    while True:
        display_header()
        print("\n1. 👨‍🎓 Student Dashboard (with AI)")
        print("2. 👨‍🏫 Teacher Dashboard (with Insights)")
        print("3. 🏛️ Admin Dashboard (with Analytics)")
        print("4. 🚪 Exit")
        print("-"*60)
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            student_dashboard()
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            teacher_dashboard()
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            admin_dashboard()
            input("\nPress Enter to continue...")
        
        elif choice == '4':
            print("\n👋 Thank you for using Education Management Portal!")
            print("   Have a great day! 🎓")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-4")
            input("\nPress Enter to continue...")

# ============================================
# RUN THE PORTAL
# ============================================

if __name__ == "__main__":
    main()