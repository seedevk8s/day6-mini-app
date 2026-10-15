"""할 일을 우선순위 순서로 보여 주는 터미널 앱."""

import sys

PRIORITY_LABELS = {1: "HIGH", 2: "MEDIUM", 3: "LOW"}


def load_tasks():
    """할 일 목록을 돌려준다. priority 는 숫자가 작을수록 높다(1이 가장 높음)."""
    return [
        {"title": "장보기", "priority": 3, "done": False},
        {"title": "보고서 제출", "priority": 1, "done": False},
        {"title": "이메일 답장", "priority": 1, "done": True},
        {"title": "운동하기", "priority": 2, "done": False},
    ]


def sort_by_priority(tasks):
    """우선순위가 높은 순서로 정렬한 새 리스트를 돌려준다. 같은 우선순위는 원래 순서를 지킨다."""
    return sorted(tasks, key=lambda task: task["priority"])


def filter_tasks(tasks, show_all):
    """미완료 할 일을 우선순위 순서로 돌려준다. show_all 이면 완료한 일을 맨 아래에 덧붙인다."""
    pending = sort_by_priority([task for task in tasks if not task["done"]])
    if not show_all:
        return pending
    done = sort_by_priority([task for task in tasks if task["done"]])
    return pending + done


def format_task(index, task):
    """할 일 하나를 '1. [HIGH] 보고서 제출' 형태의 한 줄로 만든다. 완료한 일은 끝에 (완료)를 붙인다."""
    line = f"{index}. [{PRIORITY_LABELS[task['priority']]}] {task['title']}"
    if task["done"]:
        line += " (완료)"
    return line


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    tasks = filter_tasks(load_tasks(), show_all="--all" in args)
    for index, task in enumerate(tasks, start=1):
        print(format_task(index, task))


if __name__ == "__main__":
    main()
