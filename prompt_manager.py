# 나만의 프롬프트 관리 프로그램

prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제로 이해하기 쉬운 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 제품의 특징이 잘 보이도록 구성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "광고 영상 제작 프롬프트",
        "content": "제품의 장점을 짧고 인상적으로 보여주는 광고 영상을 제작해주세요. 시각적으로 매력적인 장면으로 구성해주세요.",
        "category": "영상 생성",
        "favorite": False
    }
]

categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def show_menu():
    print("\n" + "=" * 45)
    print("       나만의 프롬프트 관리 프로그램")
    print("=" * 45)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("=" * 45)


def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목 입력: ").strip()
        if title:
            break
        print("제목은 비워둘 수 없습니다. 다시 입력해주세요.")

    while True:
        content = input("내용 입력: ").strip()
        if content:
            break
        print("내용은 비워둘 수 없습니다. 다시 입력해주세요.")

    print("\n카테고리를 선택하세요.")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    print("7. 직접 입력")

    while True:
        category_input = input("카테고리 선택: ").strip()

        if category_input.isdigit():
            number = int(category_input)

            if 1 <= number <= len(categories):
                category = categories[number - 1]
                break
            elif number == 7:
                while True:
                    category = input("카테고리 직접 입력: ").strip()
                    if category:
                        break
                    print("카테고리는 비워둘 수 없습니다.")
                break

        print("올바른 번호를 입력해주세요.")

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })

    print(f"'{title}' 프롬프트가 추가되었습니다!")


def show_list(prompt_list=None):
    print("\n=== 프롬프트 목록 ===")

    if prompt_list is None:
        prompt_list = prompts

    if not prompt_list:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompt_list, 1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f"{index}. [{prompt['category']}] {prompt['title']}{star}")

    print(f"\n총 {len(prompt_list)}개의 프롬프트")


def select_category():
    print("\n=== 카테고리별 조회 ===")

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:
        choice = input("카테고리 번호 입력: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            break

        print("올바른 번호를 입력해주세요.")

    result = [prompt for prompt in prompts if prompt["category"] == category]

    print(f"\n=== [{category}] 프롬프트 ===")

    if not result:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(result, 1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f"{index}. {prompt['title']}{star}")

    print(f"총 {len(result)}개의 프롬프트")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색할 키워드 입력: ").strip()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    result = [
        prompt for prompt in prompts
        if keyword.lower() in prompt["title"].lower()
        or keyword.lower() in prompt["content"].lower()
    ]

    if not result:
        print(f"'{keyword}'와 일치하는 프롬프트가 없습니다.")
        return

    print(f"\n=== '{keyword}' 검색 결과 ===")

    for index, prompt in enumerate(result, 1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f"{index}. [{prompt['category']}] {prompt['title']}{star}")

    print(f"총 {len(result)}개의 검색 결과")


def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    while True:
        choice = input("\n프롬프트 번호 입력 (0: 취소): ").strip()

        if choice == "0":
            return

        if choice.isdigit() and 1 <= int(choice) <= len(prompts):
            prompt = prompts[int(choice) - 1]
            star = "⭐" if prompt["favorite"] else "즐겨찾기 아님"

            print("\n" + "-" * 45)
            print(f"제목: {prompt['title']}")
            print(f"카테고리: {prompt['category']}")
            print(f"즐겨찾기: {star}")
            print(f"내용: {prompt['content']}")
            print("-" * 45)
            return

        print("잘못된 번호입니다. 다시 입력해주세요.")


def manage_favorites():
    print("\n=== 즐겨찾기 관리 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    while True:
        choice = input("\n프롬프트 번호 입력 (0: 취소): ").strip()

        if choice == "0":
            return

        if choice.isdigit() and 1 <= int(choice) <= len(prompts):
            prompt = prompts[int(choice) - 1]
            prompt["favorite"] = not prompt["favorite"]

            if prompt["favorite"]:
                print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
            else:
                print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에서 해제했습니다!")
            return

        print("잘못된 번호입니다. 다시 입력해주세요.")


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    favorites = [prompt for prompt in prompts if prompt["favorite"]]

    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(favorites, 1):
        print(f"{index}. [{prompt['category']}] {prompt['title']} ⭐")

    print(f"\n총 {len(favorites)}개의 즐겨찾기")


def main():
    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            select_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            manage_favorites()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("\n프로그램을 종료합니다. 감사합니다!")
            break
        else:
            print("\n잘못된 메뉴 번호입니다. 0~7 중에서 선택해주세요.")


if __name__ == "__main__":
    main()
