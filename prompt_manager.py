import json
from pathlib import Path


DATA_FILE = Path("prompts.json")

CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]


DEFAULT_PROMPTS = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "주어진 주제에 대해 이해하기 쉬운 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "안전 포스터 이미지 생성",
        "content": "주어진 안전 주제에 맞는 고품질 안전 포스터 이미지를 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "업무 자동화 설계",
        "content": "반복 업무를 분석하고 효율적인 자동화 방법을 설계해주세요.",
        "category": "자동화",
        "favorite": False
    }
]


def load_prompts():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return [prompt.copy() for prompt in DEFAULT_PROMPTS]


def save_prompts(prompts):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            prompts,
            file,
            ensure_ascii=False,
            indent=4
        )


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def show_list(prompts):
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        star = " ⭐" if prompt.get("favorite") else ""

        print(
            f'{i}. '
            f'[{prompt.get("category", "")}] '
            f'{prompt.get("title", "")}'
            f'{star}'
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")


def add_prompt(prompts):
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()

        if title:
            break

        print("제목은 비워둘 수 없습니다.")

    print("내용을 입력하세요.")
    print("여러 줄 입력 후 마지막 줄에 END를 입력하세요.")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    content = "\n".join(lines).strip()

    if not content:
        print("내용은 비워둘 수 없습니다.")
        return

    print("\n카테고리 선택:")

    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}) {category}")

    print("7) 직접 입력")

    while True:
        choice = input("선택: ").strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(CATEGORIES):
                category = CATEGORIES[number - 1]
                break

            elif number == 7:
                category = input("카테고리 입력: ").strip()

                if category:
                    break

        print("올바른 번호를 입력해주세요.")

    prompts.append(
        {
            "title": title,
            "content": content,
            "category": category,
            "favorite": False
        }
    )

    save_prompts(prompts)

    print("\n프롬프트가 추가되었습니다!")


def show_by_category(prompts):
    print("\n=== 카테고리별 조회 ===")

    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}) {category}")

    choice = input("선택: ").strip()

    if not choice.isdigit():
        print("올바른 번호를 입력해주세요.")
        return

    number = int(choice)

    if not 1 <= number <= len(CATEGORIES):
        print("올바른 번호를 입력해주세요.")
        return

    selected_category = CATEGORIES[number - 1]

    results = [
        (i, prompt)
        for i, prompt in enumerate(prompts, 1)
        if prompt.get("category") == selected_category
    ]

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    if not results:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for i, prompt in results:
        star = " ⭐" if prompt.get("favorite") else ""

        print(
            f'{i}. {prompt.get("title", "")}{star}'
        )

    print(f"\n총 {len(results)}개의 프롬프트")


def search_prompts(prompts):
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색어: ").strip().lower()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = [
        (i, prompt)
        for i, prompt in enumerate(prompts, 1)
        if keyword in prompt.get("title", "").lower()
        or keyword in prompt.get("content", "").lower()
    ]

    if not results:
        print("검색 결과가 없습니다.")
        return

    print("\n검색 결과:")

    for i, prompt in results:
        star = " ⭐" if prompt.get("favorite") else ""

        print(
            f'{i}. '
            f'[{prompt.get("category", "")}] '
            f'{prompt.get("title", "")}'
            f'{star}'
        )

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


def show_detail(prompts):
    print("\n=== 프롬프트 상세 보기 ===")

    text = input("프롬프트 번호 입력: ").strip()

    if not text.isdigit():
        print("올바른 번호를 입력해주세요.")
        return

    number = int(text)

    if not 1 <= number <= len(prompts):
        print("올바른 번호를 입력해주세요.")
        return

    prompt = prompts[number - 1]

    favorite = "⭐" if prompt.get("favorite") else "없음"

    print("\n────────────────────────────")
    print(f'제목: {prompt.get("title", "")}')
    print(f'카테고리: {prompt.get("category", "")}')
    print(f'즐겨찾기: {favorite}')
    print("────────────────────────────")
    print("내용:")
    print(prompt.get("content", ""))
    print("────────────────────────────")


def toggle_favorite(prompts):
    print("\n=== 즐겨찾기 관리 ===")

    show_list(prompts)

    text = input("\n프롬프트 번호 입력: ").strip()

    if not text.isdigit():
        print("올바른 번호를 입력해주세요.")
        return

    number = int(text)

    if not 1 <= number <= len(prompts):
        print("올바른 번호를 입력해주세요.")
        return

    prompt = prompts[number - 1]

    prompt["favorite"] = not prompt.get("favorite", False)

    save_prompts(prompts)

    if prompt["favorite"]:
        print(
            f'\'{prompt.get("title", "")}\' '
            f'프롬프트를 즐겨찾기에 추가했습니다!'
        )
    else:
        print(
            f'\'{prompt.get("title", "")}\' '
            f'프롬프트의 즐겨찾기를 해제했습니다!'
        )


def show_favorites(prompts):
    print("\n=== 즐겨찾기 목록 ===")

    favorites = [
        (i, prompt)
        for i, prompt in enumerate(prompts, 1)
        if prompt.get("favorite")
    ]

    if not favorites:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for i, prompt in favorites:
        print(
            f'{i}. '
            f'[{prompt.get("category", "")}] '
            f'{prompt.get("title", "")} ⭐'
        )

    print(f"\n총 {len(favorites)}개의 즐겨찾기")


def main():
    prompts = load_prompts()

    while True:
        show_menu()

        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt(prompts)

        elif choice == "2":
            show_list(prompts)

        elif choice == "3":
            show_by_category(prompts)

        elif choice == "4":
            search_prompts(prompts)

        elif choice == "5":
            show_detail(prompts)

        elif choice == "6":
            toggle_favorite(prompts)

        elif choice == "7":
            show_favorites(prompts)

        elif choice == "0":
            print("\n프로그램을 종료합니다.")
            break

        else:
            print("\n잘못된 번호입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()