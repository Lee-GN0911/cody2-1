# 프롬프트 데이터를 저장할 리스트
prompts = []

def display_menu():
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def add_prompt():
    print("\n--- 프롬프트 추가 ---")
    title = input("제목: ")
    category = input("카테고리: ")
    content = input("내용: ")
    
    # is_favorite 초기값 False 추가
    prompt = {
        "title": title,
        "category": category,
        "content": content,
        "is_favorite": False
    }
    prompts.append(prompt)
    print(">> 프롬프트가 성공적으로 추가되었습니다!\n")

def list_prompts():
    print("\n--- 프롬프트 목록 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.\n")
        return
    
    for idx, p in enumerate(prompts, 1):
        print(f"{idx}. [{p['category']}] {p['title']}")
    print()

def view_by_category():
    print("\n--- 카테고리별 조회 ---")
    category_to_find = input("조회할 카테고리명: ")
    found = False
    
    for idx, p in enumerate(prompts, 1):
        if p["category"] == category_to_find:
            print(f"{idx}. {p['title']}")
            found = True
            
    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")
    print()

def search_prompt():
    print("\n--- 프롬프트 검색 ---")
    keyword = input("검색어: ")
    found = False
    
    for idx, p in enumerate(prompts, 1):
        if keyword in p["title"] or keyword in p["content"]:
            print(f"{idx}. [{p['category']}] {p['title']}")
            found = True
            
    if not found:
        print("검색어가 포함된 프롬프트가 없습니다.")
    print()

def view_prompt_detail():
    print("\n--- 프롬프트 상세 보기 ---")
    try:
        idx = int(input("조회할 프롬프트 번호: "))
        if 1 <= idx <= len(prompts):
            p = prompts[idx - 1]
            fav_status = "⭐ 등록됨" if p["is_favorite"] else "☆ 미등록"
            
            print("\n[상세 정보]")
            print(f"제목: {p['title']}")
            print(f"카테고리: {p['category']}")
            print(f"즐겨찾기: {fav_status}")
            print(f"내용:\n{p['content']}")
        else:
            print(">> 오류: 존재하지 않는 프롬프트 번호입니다.")
    except ValueError:
        print(">> 오류: 유효한 숫자를 입력해 주세요.")
    print()

def manage_favorite():
    print("\n--- 즐겨찾기 관리 ---")
    try:
        idx = int(input("상태를 변경할 프롬프트 번호: "))
        if 1 <= idx <= len(prompts):
            p = prompts[idx - 1]
            p["is_favorite"] = not p["is_favorite"] # 상태 반전
            
            status_msg = "등록" if p["is_favorite"] else "해제"
            print(f">> '{p['title']}' 프롬프트가 즐겨찾기에 {status_msg}되었습니다.")
        else:
            print(">> 오류: 존재하지 않는 프롬프트 번호입니다.")
    except ValueError:
        print(">> 오류: 유효한 숫자를 입력해 주세요.")
    print()

def list_favorites():
    print("\n--- 즐겨찾기 목록 ---")
    found = False
    
    for idx, p in enumerate(prompts, 1):
        if p["is_favorite"]:
            print(f"{idx}. [{p['category']}] {p['title']}")
            found = True
            
    if not found:
        print("즐겨찾기에 등록된 프롬프트가 없습니다.")
    print()

def main():
    while True:
        display_menu()
        choice = input("선택: ")
        
        if choice == '1':
            add_prompt()
        elif choice == '2':
            list_prompts()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            search_prompt()
        elif choice == '5':
            view_prompt_detail()
        elif choice == '6':
            manage_favorite()
        elif choice == '7':
            list_favorites()
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해 주세요.\n")

if __name__ == "__main__":
    main()