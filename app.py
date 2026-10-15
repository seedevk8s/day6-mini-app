"""할 일을 우선순위 순서로 보여 주는 터미널 앱."""


def load_tasks():
    """할 일 목록을 돌려준다. priority 는 숫자가 작을수록 높다(1이 가장 높음)."""
    return [
        {"title": "장보기", "priority": 3},
        {"title": "보고서 제출", "priority": 1},
        {"title": "운동하기", "priority": 2},
        {"title": "이메일 정리", "priority": 3},
        {"title": "회의 준비", "priority": 1},
    ]


def sort_by_priority(tasks):
    """우선순위가 높은 순서로 정렬한 새 리스트를 돌려준다. 같은 우선순위는 원래 순서를 지킨다."""
    return sorted(tasks, key=lambda task: task["priority"])


def format_task(index, task):
    """할 일 하나를 '1. [P1] 보고서 제출' 형태의 한 줄로 만든다."""
    return f"{index}. [P{task['priority']}] {task['title']}"


def main():
    tasks = sort_by_priority(load_tasks())
    for index, task in enumerate(tasks, start=1):
        print(format_task(index, task))


if __name__ == "__main__":
    main()
