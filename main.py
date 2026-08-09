# 프롬프트 데이터를 저장할 리스트
prompts = []

def display_menu():
    # 모든 작업 완료/취소 후 메인 메뉴가 뜨기 직전에 항상 출력되는 구분선
    print("\n--------------------------CLEAR------------------------")
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 수정")
    print("3. 프롬프트 목록")
    print("4. 카테고리별 조회")
    print("5. 프롬프트 검색")
    print("6. 프롬프트 상세 보기")
    print("7. 즐겨찾기 관리")
    print("8. 즐겨찾기 목록")
    print("0. 종료")

def add_prompt():
    print("\n--- 프롬프트 추가 ---")
    print("(* 0: 완전 취소 후 메인메뉴, <: 이전 단계로 돌아가기)")
    
    title, category, content = "", "", ""
    step = 1
    
    while step <= 3:
        if step == 1:
            val = input(f"1. 제목 (현재: {title}) : " if title else "1. 제목 : ")
            if val == '0': 
                print(">> 추가 작업이 취소되었습니다."); return
            if val == '<': 
                print(">> 첫 번째 항목입니다."); continue
            
            if val.strip(): 
                title = val
                step += 1
            elif not title: 
                print(">> 공백. 재입력 바랍니다."); continue
            else:
                step += 1
                
        elif step == 2:
            val = input(f"2. 카테고리 (현재: {category}) : " if category else "2. 카테고리 : ")
            if val == '0': 
                print(">> 추가 작업이 취소되었습니다."); return
            if val == '<': 
                step -= 1; continue
            
            if val.strip(): 
                category = val
                step += 1
            elif not category: 
                print(">> 공백. 재입력 바랍니다."); continue
            else:
                step += 1
                
        elif step == 3:
            val = input(f"3. 내용 (현재: {content}) : " if content else "3. 내용 : ")
            if val == '0': 
                print(">> 추가 작업이 취소되었습니다."); return
            if val == '<': 
                step -= 1; continue
                
            if val.strip(): 
                content = val
                step += 1
            elif not content: 
                print(">> 공백. 재입력 바랍니다."); continue
            else:
                step += 1
    
    prompt = {
        "title": title,
        "category": category,
        "content": content,
        "is_favorite": False
    }
    prompts.append(prompt)
    print(">> 프롬프트가 성공적으로 추가되었습니다!")

def list_prompts():
    print("\n--- 프롬프트 목록 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    
    for idx, p in enumerate(prompts, 1):
        print(f"{idx}. [{p['category']}] {p['title']}")

def edit_prompt():
    print("\n--- 프롬프트 수정 ---")
    if not prompts:
        print("수정할 프롬프트가 없습니다.")
        return
        
    print("1. 번호 바로 입력")
    print("2. 목록 조회 후 입력")
    sub_choice = input("선택 (1 또는 2, 취소: 0): ")
    
    if sub_choice == '0':
        print(">> 수정 작업이 취소되었습니다.")
        return
    elif sub_choice == '2':
        list_prompts()
        print() # 간격 조절용
    elif sub_choice != '1':
        print(">> 잘못된 입력입니다. 메인 메뉴로 돌아갑니다.")
        return
        
    try:
        idx_str = input("수정할 프롬프트 번호 (취소: 0): ")
        if idx_str == '0':
            print(">> 수정 작업이 취소되었습니다.")
            return
            
        idx = int(idx_str)
        if 1 <= idx <= len(prompts):
            p = prompts[idx - 1]
            
            print("\n(* 0: 완전 취소, <: 이전 항목으로, Enter: 기존 내용 유지)")
            title, category, content = p['title'], p['category'], p['content']
            step = 1
            
            while step <= 3:
                if step == 1:
                    val = input(f"1. 제목 [현재: {title}]: ")
                    if val == '0': print(">> 수정이 취소되었습니다."); return
                    if val == '<': print(">> 첫 번째 항목입니다."); continue
                    if val.strip(): title = val
                    step += 1
                elif step == 2:
                    val = input(f"2. 카테고리 [현재: {category}]: ")
                    if val == '0': print(">> 수정이 취소되었습니다."); return
                    if val == '<': step -= 1; continue
                    if val.strip(): category = val
                    step += 1
                elif step == 3:
                    val = input(f"3. 내용 [현재: {content}]: ")
                    if val == '0': print(">> 수정이 취소되었습니다."); return
                    if val == '<': step -= 1; continue
                    if val.strip(): content = val
                    step += 1
                    
            p['title'], p['category'], p['content'] = title, category, content
            print(f">> {idx}번 프롬프트가 성공적으로 수정되었습니다!")
        else:
            print(">> 오류: 존재하지 않는 프롬프트 번호입니다.")
    except ValueError:
        print(">> 오류: 유효한 숫자를 입력해 주세요.")

def view_by_category():
    print("\n--- 카테고리별 조회 ---")
    category_to_find = input("조회할 카테고리명 (취소: 0): ")
    if category_to_find == '0':
        print(">> 조회 작업이 취소되었습니다.")
        return
        
    found = False
    
    for idx, p in enumerate(prompts, 1):
        if p["category"] == category_to_find:
            print(f"{idx}. {p['title']}")
            found = True
            
    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")

def search_prompt():
    print("\n--- 프롬프트 검색 ---")
    keyword = input("검색어 (취소: 0): ")
    if keyword == '0':
        print(">> 검색 작업이 취소되었습니다.")
        return
        
    found = False
    
    for idx, p in enumerate(prompts, 1):
        if keyword in p["title"] or keyword in p["content"]:
            print(f"{idx}. [{p['category']}] {p['title']}")
            found = True
            
    if not found:
        print("검색어가 포함된 프롬프트가 없습니다.")

def view_prompt_detail():
    print("\n--- 프롬프트 상세 보기 ---")
    try:
        idx_str = input("조회할 프롬프트 번호 (취소: 0): ")
        if idx_str == '0':
            print(">> 조회 작업이 취소되었습니다.")
            return
            
        idx = int(idx_str)
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

def manage_favorite():
    print("\n--- 즐겨찾기 관리 ---")
    try:
        idx_str = input("상태를 변경할 프롬프트 번호 (취소: 0): ")
        if idx_str == '0':
            print(">> 작업이 취소되었습니다.")
            return
            
        idx = int(idx_str)
        if 1 <= idx <= len(prompts):
            p = prompts[idx - 1]
            p["is_favorite"] = not p["is_favorite"]
            
            status_msg = "등록" if p["is_favorite"] else "해제"
            print(f">> '{p['title']}' 프롬프트가 즐겨찾기에 {status_msg}되었습니다.")
        else:
            print(">> 오류: 존재하지 않는 프롬프트 번호입니다.")
    except ValueError:
        print(">> 오류: 유효한 숫자를 입력해 주세요.")

def list_favorites():
    print("\n--- 즐겨찾기 목록 ---")
    found = False
    
    for idx, p in enumerate(prompts, 1):
        if p["is_favorite"]:
            print(f"{idx}. [{p['category']}] {p['title']}")
            found = True
            
    if not found:
        print("즐겨찾기에 등록된 프롬프트가 없습니다.")

def main():
    while True:
        display_menu()
        choice = input("선택: ")
        
        if choice == '1':
            add_prompt()
        elif choice == '2':
            edit_prompt()
        elif choice == '3':
            list_prompts()
        elif choice == '4':
            view_by_category()
        elif choice == '5':
            search_prompt()
        elif choice == '6':
            view_prompt_detail()
        elif choice == '7':
            manage_favorite()
        elif choice == '8':
            list_favorites()
        elif choice == '0':
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("\n>> 잘못된 입력입니다. 다시 선택해 주세요.")

if __name__ == "__main__":
    main()