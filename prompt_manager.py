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

while True:
    print("=== 프롬프트 관리 ===")
    print("1. 프롬프트 목록 보기")
    print("2. 프롬프트 추가")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

    choice = input("선택: ")

    if choice == "1":
        number = 1

        for prompt in prompts:
            print(number, prompt["category"], prompt["title"])
            number = number + 1

    elif choice == "2":
        title = input("제목: ")
        content = input("내용: ")
        category = input("카테고리: ")

        new_prompt = {
            "title": title,
            "content": content,
            "category": category,
            "favorite": False
        }

        prompts.append(new_prompt)
        print("프롬프트가 추가되었습니다.")

    elif choice == "3":
        category = input("카테고리 입력: ")

        for prompt in prompts:
            if prompt["category"] == category:
                print(prompt["title"])

    elif choice == "4":
        keyword = input("검색어: ")

        for prompt in prompts:
            if keyword in prompt["title"] or keyword in prompt["content"]:
                print(prompt["title"])

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
      

