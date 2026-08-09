# 프로그램 시작 시 기본으로 제공될 프롬프트 데이터 (더미 데이터)
prompts = [
    {
        "title": "프롬프트 엔지니어링 기초",
        "category": "가이드",
        "content": "AI 모델에게 명확한 역할(Role)을 부여하고, 구체적인 제약 사항과 출력 형식(Format)을 지정하여 원하는 결과물의 품질을 높이는 기본 작성 가이드입니다.",
        "is_favorite": True
    },
    {
        "title": "하네스 엔지니어링 기초",
        "category": "가이드",
        "content": "시스템 테스트 환경 구축을 위한 테스트 하네스(Test Harness)의 개념, 그리고 스텁(Stub)과 드라이버(Driver)를 활용한 모듈 검증 방법에 대한 기초 자료입니다.",
        "is_favorite": False
    },
    {
        "title": "업무분담 원칙",
        "category": "가이드",
        "content": "프로젝트 진행 시 각 팀원의 R&R(Role and Responsibilities)을 명확히 정의하고, 중복 및 누락되는 업무를 방지하기 위한 작업 분배 및 커뮤니케이션 기준입니다.",
        "is_favorite": False
    },
    {
        "title": "회의록 초안 작성 프롬프트",
        "category": "자동화",
        "content": "회의 중 작성한 거친 메모를 붙여넣으면, '주요 안건', '결정 사항(Action Item)', '향후 일정'의 3가지 항목으로 자동 분류하여 마크다운 형식으로 정리해 주는 프롬프트입니다.",
        "is_favorite": True
    }
]

def wait_for_zero():
    """사용자가 0을 입력할 때까지 대기하는 함수"""
    while True:
        print("\n--- Action ---")
        if input("메인 메뉴로 돌아가려면 0을 입력하세요: ") == '0':
            break

def display_menu():
    print("\n--------------------------CLEAR------------------------")
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 수정")
    print("3. 프롬프트 목록")
    print("4. 카테고리별 조회")
    print("5. 프롬프트 검색")
    print("6. 프롬프트 상세 보기")
    print("7. 즐겨찾기 등록/해제")
    print("8. 즐겨찾기 목록")
    print("0. 종료")

def add_prompt():
    print("\n--- 프롬프트 추가 ---")
    print("(* 0: 완전 취소 후 메인메뉴, <: 이전 단계로 돌아가기)")
    
    title, category, content = "", "", ""
    step = 1
    
    while step <= 3:
        print("\n--- Action ---")
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

def show_detail_by_idx(idx):
    """특정 인덱스의 상세 정보를 출력하는 공통 함수"""
    if 1 <= idx <= len(prompts):
        p = prompts[idx - 1]
        fav_status = "⭐ 등록됨" if p["is_favorite"] else "☆ 미등록"
        
        print("\n[상세 정보]")
        print(f"제목: {p['title']}")
        print(f"카테고리: {p['category']}")
        print(f"즐겨찾기: {fav_status}")
        print(f"내용:\n{p['content']}")
        return True
    else:
        print(">> 오류: 존재하지 않는 프롬프트 번호입니다.")
        return False

def list_prompts(interactive=False):
    print("\n--- 프롬프트 목록 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        if interactive:
            wait_for_zero()
        return
    
    for idx, p in enumerate(prompts, 1):
        star = " ★" if p["is_favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']}{star}")
        
    if interactive:
        print("\n--- Action ---")
        print("1. 조회할 프롬프트 번호 입력")
        print("0. 메인메뉴로")
        choice = input("선택: ")
        
        if choice == '1':
            print("\n--- Action ---")
            try:
                idx = int(input("조회할 프롬프트 번호: "))
                if show_detail_by_idx(idx):
                    wait_for_zero()
                else:
                    wait_for_zero()
            except ValueError:
                print(">> 오류: 유효한 숫자를 입력해 주세요.")
                wait_for_zero()
        elif choice != '0':
            print(">> 잘못된 입력입니다.")
            wait_for_zero()

def edit_prompt():
    print("\n--- 프롬프트 수정 ---")
    if not prompts:
        print("수정할 프롬프트가 없습니다.")
        return
        
    for idx, p in enumerate(prompts, 1):
        star = " ★" if p["is_favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']}{star}")
        
    print("\n--- Action ---")
    print("1. 수정할 프롬프트 번호 입력")
    print("0. 메인메뉴로")
    sub_choice = input("선택: ")
    
    if sub_choice == '0':
        print(">> 수정 작업이 취소되었습니다.")
        return
    elif sub_choice != '1':
        print(">> 잘못된 입력입니다. 메인 메뉴로 돌아갑니다.")
        return
        
    print("\n--- Action ---")
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
                print("\n--- Action ---")
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
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        wait_for_zero()
        return
        
    categories = []
    for p in prompts:
        if p["category"] not in categories:
            categories.append(p["category"])
            
    print("등록된 카테고리 목록:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    print("0. 메인메뉴로")
    
    print("\n--- Action ---")
    cat_choice = input("조회할 카테고리 번호 선택: ")
    if cat_choice == '0':
        return
        
    try:
        cat_idx = int(cat_choice)
        if 1 <= cat_idx <= len(categories):
            selected_cat = categories[cat_idx - 1]
            print(f"\n[{selected_cat} 카테고리 목록]")
            
            matched_prompts = []
            display_num = 1
            for real_idx, p in enumerate(prompts):
                if p["category"] == selected_cat:
                    matched_prompts.append((display_num, real_idx, p))
                    star = " ★" if p["is_favorite"] else ""
                    print(f"{display_num}. {p['title']}{star}")
                    display_num += 1
            
            print("\n--- Action ---")
            print("1. 조회할 프롬프트 번호 입력")
            print("0. 메인메뉴로")
            sub_choice = input("선택: ")
            
            if sub_choice == '1':
                print("\n--- Action ---")
                try:
                    p_num = int(input("조회할 프롬프트 번호: "))
                    target_real_idx = None
                    for disp_num, r_idx, _ in matched_prompts:
                        if disp_num == p_num:
                            target_real_idx = r_idx + 1
                            break
                            
                    if target_real_idx is not None:
                        show_detail_by_idx(target_real_idx)
                    else:
                        print(">> 오류: 해당 카테고리에 존재하지 않는 번호입니다.")
                except ValueError:
                    print(">> 오류: 유효한 숫자를 입력해 주세요.")
            
            wait_for_zero()
        else:
            print(">> 오류: 잘못된 번호입니다.")
            wait_for_zero()
    except ValueError:
        print(">> 오류: 유효한 숫자를 입력해 주세요.")
        wait_for_zero()

def search_prompt():
    print("\n--- 프롬프트 검색 ---")
    while True:
        print("\n--- Action ---")
        keyword = input("검색어 (메인메뉴로: 0): ")
        
        if keyword == '0':
            print(">> 검색 작업이 종료되었습니다.")
            return
            
        matched_results = []
        for idx, p in enumerate(prompts, 1):
            if keyword in p["title"] or keyword in p["content"]:
                matched_results.append((idx, p))
                
        if not matched_results:
            print(">> 검색어가 포함된 프롬프트가 없습니다. 다시 검색해 주세요.")
        else:
            print() 
            for idx, p in enumerate(matched_results, 1):
                star = " ★" if p[1]["is_favorite"] else ""
                print(f"{idx}. [{p[1]['category']}] {p[1]['title']}{star}")
                
            print("\n--- Action ---")
            print("1. 조회할 프롬프트 번호 입력")
            print("0. 메인메뉴로")
            sub_choice = input("선택: ")
            
            if sub_choice == '1':
                print("\n--- Action ---")
                try:
                    p_num = int(input("조회할 프롬프트 번호: "))
                    if 1 <= p_num <= len(matched_results):
                        real_idx = matched_results[p_num - 1][0]
                        show_detail_by_idx(real_idx)
                        wait_for_zero()
                        return
                    else:
                        print(">> 오류: 존재하지 않는 프롬프트 번호입니다.")
                        wait_for_zero()
                        return
                except ValueError:
                    print(">> 오류: 유효한 숫자를 입력해 주세요.")
                    wait_for_zero()
                    return
            elif sub_choice == '0':
                return
            else:
                print(">> 잘못된 입력입니다.")
                wait_for_zero()
                return

def view_prompt_detail():
    print("\n--- 프롬프트 상세 보기 ---")
    if not prompts:
        print("조회할 프롬프트가 없습니다.")
        return
        
    print("--- Action ---")
    print("1. 번호 바로 입력")
    print("2. 목록 조회 후 입력")
    print("0. 취소")
    sub_choice = input("선택: ")
    
    if sub_choice == '0':
        print(">> 조회 작업이 취소되었습니다.")
        return
    elif sub_choice == '2':
        list_prompts(interactive=False)
        print() 
    elif sub_choice != '1':
        print(">> 잘못된 입력입니다. 메인 메뉴로 돌아갑니다.")
        return
        
    print("\n--- Action ---")
    try:
        idx_str = input("조회할 프롬프트 번호 (취소: 0): ")
        if idx_str == '0':
            print(">> 조회 작업이 취소되었습니다.")
            return
            
        idx = int(idx_str)
        if show_detail_by_idx(idx):
            wait_for_zero()
    except ValueError:
        print(">> 오류: 유효한 숫자를 입력해 주세요.")

def manage_favorite():
    print("\n--- 즐겨찾기 등록/해제 ---")
    if not prompts:
        print("설정할 프롬프트가 없습니다.")
        return
        
    # 진입하자마자 목록 출력
    for idx, p in enumerate(prompts, 1):
        star = " ★" if p["is_favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']}{star}")
        
    print("\n--- Action ---")
    print("1. 즐겨찾기 등록/변경")
    print("0. 메인메뉴")
    sub_choice = input("선택: ")
    
    if sub_choice == '0':
        print(">> 작업이 취소되었습니다.")
        return
    elif sub_choice != '1':
        print(">> 잘못된 입력입니다. 메인 메뉴로 돌아갑니다.")
        return
        
    print("\n--- Action ---")
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
    while True:
        print("\n--- 즐겨찾기 목록 ---")
        found = False
        
        for idx, p in enumerate(prompts, 1):
            if p["is_favorite"]:
                print(f"{idx}. [{p['category']}] {p['title']} ★")
                found = True
                
        if not found:
            print("즐겨찾기에 등록된 프롬프트가 없습니다.")
            wait_for_zero()
            return
            
        print("\n--- Action ---")
        print("1. 조회할 프롬프트 번호 입력")
        print("0. 메인메뉴로")
        choice = input("선택: ")
        
        if choice == '1':
            print("\n--- Action ---")
            try:
                idx = int(input("조회할 프롬프트 번호: "))
                if 1 <= idx <= len(prompts) and prompts[idx - 1]["is_favorite"]:
                    show_detail_by_idx(idx)
                    wait_for_zero()
                    return
                else:
                    print(">> 오류: 즐겨찾기 목록에 존재하지 않는 번호입니다.")
                    print("\n--- Action ---")
                    print("1. 재선택")
                    print("0. 메인 메뉴로")
                    err_choice = input("선택: ")
                    if err_choice == '0':
                        return
            except ValueError:
                print(">> 오류: 유효한 숫자를 입력해 주세요.")
                print("\n--- Action ---")
                print("1. 재선택")
                print("0. 메인 메뉴로")
                err_choice = input("선택: ")
                if err_choice == '0':
                    return
        elif choice == '0':
            return
        else:
            print(">> 잘못된 입력입니다.")
            wait_for_zero()
            return

def main():
    while True:
        display_menu()
        print("\n--- Action ---")
        choice = input("선택: ")
        
        if choice == '1':
            add_prompt()
        elif choice == '2':
            edit_prompt()
        elif choice == '3':
            list_prompts(interactive=True)
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