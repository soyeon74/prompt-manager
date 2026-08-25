prompts = [
    {
        "title": "블로그 작성",
        "content": "SEO에 맞는 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "제품 이미지 생성",
        "content": "제품의 특징이 잘 보이는 이미지를 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "광고 영상 만들기",
        "content": "제품 광고용 영상 아이디어를 만들어주세요.",
        "category": "영상 생성",
        "favorite": False
    }
]

def show_menu():
    print("=== 프롬프트 관리 ===")
    print("1. 프롬프트 목록 보기")
    print("2. 프롬프트 추가")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def show_list():
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
    else:
        print("=== 프롬프트 목록 ===")

        for number, prompt in enumerate(prompts, start=1):
            favorite_mark = "⭐" if prompt["favorite"] else ""
            print(f'{number}. [{prompt["category"]}] {prompt["title"]} {favorite_mark}')

        print("총", len(prompts), "개의 프롬프트가 등록되어 있습니다.")

def add_prompt():
    print("=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()

        if title != "":
            break

        print("제목은 비워둘 수 없습니다.")

    print("내용을 입력하세요.")
    print("여러 줄을 입력할 수 있습니다.")
    print("입력이 끝나면 마지막 줄에 END를 입력하세요.")

    content_lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        content_lines.append(line)

    content = "\n".join(content_lines).strip()

    if content == "":
        print("내용은 비워둘 수 없습니다.")
        return

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    print("카테고리 선택:")

    for number, category_name in enumerate(categories, start=1):
        print(f"{number}) {category_name}")

    print("7) 직접 입력")

    while True:
        category_choice = input("선택: ").strip()

        if category_choice.isdigit():
            category_number = int(category_choice)

            if 1 <= category_number <= len(categories):
                category = categories[category_number - 1]
                break

            elif category_number == 7:
                while True:
                    category = input("새 카테고리 입력: ").strip()

                    if category != "":
                        break

                    print("카테고리는 비워둘 수 없습니다.")

                break

        print("올바른 번호를 입력해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("프롬프트가 추가되었습니다.")


def show_by_category():
    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    print("=== 카테고리별 조회 ===")

    for number, category_name in enumerate(categories, start=1):
        print(f"{number}) {category_name}")

    category_choice = input("선택: ").strip()

    if category_choice.isdigit():
        category_number = int(category_choice)

        if 1 <= category_number <= len(categories):
            selected_category = categories[category_number - 1]

            found_count = 0

            print(f"[{selected_category}] 카테고리 프롬프트:")

            for number, prompt in enumerate(prompts, start=1):
                if prompt["category"] == selected_category:
                    favorite_mark = "⭐" if prompt["favorite"] else ""
                    print(f'{number}. {prompt["title"]} {favorite_mark}')
                    found_count = found_count + 1

            if found_count == 0:
                print("해당 카테고리에 등록된 프롬프트가 없습니다.")
            else:
                print("총", found_count, "개의 프롬프트")

        else:
            print("올바른 카테고리 번호를 입력해주세요.")

    else:
        print("숫자를 입력해주세요.")


while True:
    show_menu() 
    
    choice = input("선택: ")

    if choice == "1":
        show_list()
            
    elif choice == "2":
        add_prompt()

    elif choice == "3":
        show_by_category()

    elif choice == "4":
        keyword = input("검색어: ").strip().lower()

        found_count = 0

        print("=== 검색 결과 ===")

        for number, prompt in enumerate(prompts, start=1):
            title = prompt["title"].lower()
            content = prompt["content"].lower()

            if keyword in title or keyword in content:
                favorite_mark = "⭐" if prompt["favorite"] else ""
                print(f'{number}. [{prompt["category"]}] {prompt["title"]} {favorite_mark}')
                found_count = found_count + 1

        if found_count == 0:
            print("검색 결과가 없습니다.")
        else:
            print("총", found_count, "개의 프롬프트를 찾았습니다.")

    elif choice == "5":
        number_text = input("프롬프트 번호: ")

        if number_text.isdigit():
            number = int(number_text)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]

                print("제목:", prompt["title"])
                print("카테고리:", prompt["category"])
                print("즐겨찾기:", prompt["favorite"])
                print("내용:", prompt["content"])
            else:
                print("존재하지 않는 프롬프트 번호입니다.")
        else:
            print("숫자를 입력해주세요.") 

    elif choice == "6":
        number_text = input("프롬프트 번호: ")

        if number_text.isdigit():
            number = int(number_text)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]

                prompt["favorite"] = not prompt["favorite"]

                if prompt["favorite"]:
                    print("즐겨찾기에 추가되었습니다.")
                else:
                    print("즐겨찾기에서 해제되었습니다.")
            else:
                print("존재하지 않는 프롬프트 번호입니다.")
        else:
            print("숫자를 입력해주세요.")

    elif choice == "7":
        favorite_count = 0

        for number, prompt in enumerate(prompts, start=1):
            if prompt["favorite"]:
                print(number, prompt["category"], prompt["title"], "⭐")
                favorite_count = favorite_count + 1

        if favorite_count == 0:
            print("즐겨찾기된 프롬프트가 없습니다.")
        else:
            print("총", favorite_count, "개의 즐겨찾기")

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 번호입니다. 다시 선택해주세요.")            
                 
      

