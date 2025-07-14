class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        from collections import Counter 

        student_count = Counter(students)

        count = 0
        while students:
            sandwich = sandwiches[0]
            
            if(student_count[sandwich] == 0):
                return n - count

            expected = students.pop(0)
            
            if(sandwich == expected):
                student_count[expected] -= 1
                sandwiches.pop(0)
                count += 1
            else:
                students.append(expected)

        return n - count