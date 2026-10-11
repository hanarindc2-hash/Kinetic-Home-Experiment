from pathlib import Path
import json

base=Path(__file__).resolve().parent/'kinetic-garden'
p=base/'garden-board.json'
d=json.loads(p.read_text(encoding='utf-8'))
sources={
'ARC-01':('Vitsœ 606','https://www.vitsoe.com/gb/606'),
'ARC-02':('Vitsœ 구조','https://www.vitsoe.com/gb/606/structures'),
'ARC-03':('Vitsœ FAQ','https://www.vitsoe.com/us/faqs'),
'ARC-04':('Vitsœ Good design','https://www.vitsoe.com/gb/about/good-design'),
'ARC-05':('Vitsœ 거래 조건','https://www.vitsoe.com/us/terms-and-conditions'),
'ARC-06':('Vitsœ 일본어 FAQ','https://www.vitsoe.com/jp/faqs'),
'REF-01':('USM 역사 · 독일어','https://www.usm.com/de-de/ueber-usm/geschichte'),
'REF-02':('USM World of Plants','https://www.usm.com/en-uk/collections/usm-haller-system/world-of-plants'),
'REF-03':('USM 식재 설명 PDF','https://www.usm.com/media/12665/aworldofplants_usm_haller_operating_instructions_en.pdf'),
'REF-04':('Habraken The Uses of Levels','https://habraken.com/html/downloads/the_uses_of_levels.pdf'),
'REF-05':('Bosch Rexroth · 프랑스어','https://expertise.boschrexroth.fr/profiles-aluminium/profiles-aluminium-standard/'),
'REF-06':('GARDENA Water Stop','https://us.gardena.com/collections/quick-connect-system/products/gardena-18218'),
'REF-07':('Neutrik 기존 TRUE1 TOP','https://www.neutrik.com/en/product/nac3fx-w-top'),
'REF-08':('Neutrik TRUE1 S','https://www.neutrik.co.uk/product/nac3f-true1-s')}
def card(cid,title,body,status,refs=()):
 return {'id':cid,'title':title,'body':body,'status':status,'sources':[{'label':key+' · '+sources[key][0],'url':sources[key][1]} for key in refs]}
new=[
{'id':'arc_606','title':'R01 606 설치와 장기 사용','intro':'비초에 606을 핵심 아키텍처 레퍼런스로 채택한다. 정원의 형태·규격·실제 부품 채택은 미정이다.','color':'#E8EDF6','cards':[
 card('intuition','사용자의 건축적 직감','설치, 오래 쓰는 목적, 선반의 조합이 하나의 건축처럼 느껴진다는 직감을 연구의 출발점으로 삼는다. 오래 유지하는 기반 위에서 생활과 식생 구성을 바꾸는 시스템으로 연결할 수 있다.','사용자 인사이트·해석'),
 card('structure','설치한 기준과 핀 결합','1960년 Dieter Rams 설계. E-Track을 벽이나 포스트에 두고 핀으로 선반·캐비닛·작업면을 구성한다. E-Track은 고정·재배치 기반이며 화분을 모터로 주행시키는 이송 레일은 아니다.','공식 자료 확인',['ARC-01','ARC-02']),
 card('longlife','시스템과 부품의 수명','FAQ는 오래된 부품과 새 부품의 호환, 이사와 재구성, 상담·도면 보관을 설명한다. 거래 조건은 과거의 모든 부품 공급을 보장하지 않는다. 호환성과 영구 공급은 구분해서 연구한다.','공식 설명·경계',['ARC-03','ARC-05','ARC-06']),
 card('form','조형의 질서를 전이하기','브루탈리즘처럼 읽힌다는 인상은 사용자의 조형 해석이다. 역사적 분류로 단정하지 않는다. 반복 구조·수평면·접합·빈칸을 식생의 밀도와 비교한다. 콘크리트나 거친 표면은 아직 필수 재료가 아니다.','해석·심미성 가설'),
 card('transfer','정원으로 가져올 원리','설치 기준과 교체 모듈, 부분 확장, 결합 상태의 가시성, 부품과 도면 기록을 함께 연구한다. 프레임은 유지하면서 식물·펌프·센서·조명을 바꿀 수 있는지는 조건별로 확인한다.','제안·검증 전',['ARC-04']),
 card('limits','설치와 습기의 경계','원문은 설치 기반의 강도, 구성 변경 절차와 과도한 습기 노출의 경계를 설명한다. 606의 조립 원리를 정원의 설치·젖은 하중·누수·구동 성능 근거로 대신 사용할 수는 없다.','적용 경계',['ARC-02','ARC-03'])]},
{'id':'arc_candidates','title':'R02 추가 후보 5개','intro':'제품·건축 이론·물리적 사용자 인터페이스를 비교한다. 영어·독일어·프랑스어 등 원문 근거와 설계 해석을 구분한다.','color':'#FFF1DC','cards':[
 card('usm','1 USM Haller와 식재 모듈','건축의 모듈 문법을 가구로 전개한 사례이며 World of Plants는 기존 Haller에 식재를 더한다. 가구와 식물을 합친 대안은 이미 존재한다. 성장하는 경계·돌봄·사용자의 변경 권한에서 우리 차이를 확인한다.','확인·경쟁 비교 후보',['REF-01','REF-02','REF-03']),
 card('habraken','2 Habraken Supports','The Uses of Levels는 기반과 내부 구성의 수준, 설계·사용 중 통제권을 다룬다. 오래 유지할 설비와 바꾸어 쓸 모듈뿐 아니라 누가 바꿀 수 있는지를 계획하는 이론 후보다. 형태 레퍼런스는 아니다.','확인·권한 분석 후보',['REF-04']),
 card('profiles','3 Bosch Rexroth 프로파일','표준 프레임과 연결 부품을 용접 없이 조합·변경하는 산업 시스템. 식재·조명·수납·제한 구동을 더하고 제거하는 모형 기반으로 연구한다. 단면·브랜드·젖은 주거 하중 적합성은 아직 선정·검증 전이다.','확인·구조 모형 후보',['REF-05']),
 card('waterstop','4 GARDENA Water Stop','액세서리 분리와 물 공급 차단을 연결하는 PUI. 사용자 동작과 설비 상태가 이어지는 원리를 관찰한다. 흐름 차단과 잔수 제거는 다르며 정원 호스용 설명을 실내 무누수 보증으로 사용하지 않는다.','확인·물 연결 PUI 후보',['REF-06']),
 card('neutrik','5 Neutrik TRUE1','방향 구분과 의도적인 잠금·해제의 전원 연결 PUI. 기존 모델의 단계적 종료와 후속 모델은 장수명 시스템의 부품 세대 관리도 보여준다. 첫 모형은 전기를 연결하지 않고 조작만 비교한다.','확인·잠금 PUI 후보',['REF-07','REF-08']),
 card('choose','고르는 기준을 남기기','606+Habraken: 기반과 권한. USM: 기존 식재 가구와 차이. 프로파일: 물리적 구조 모형. GARDENA·Neutrik: 연결·해제 경험. 모두 채택할 필요는 없다. 먼저 볼 후보와 이유: __________','사용자 선택·미정')]},
{'id':'arc_pui','title':'R03 접점과 오래 쓰는 방법','intro':'PUI는 여기서 잡기·끼우기·잠그기·풀기·상태 읽기를 포함한 물리적 사용자 인터페이스로 해석한다.','color':'#E8F7F1','cards':[
 card('physical','손으로 바꾸는 경험','구조가 충분히 고정되었는지, 해제하면 무엇이 움직이는지, 연결 방향이 맞는지를 보여줄 수 있는가? 잡는 면·양손 접근·잠금 상태를 비교한다. 공구 없는 변경과 공구 없는 최초 설치를 구분한다.','조작·사용성 가설'),
 card('service','물과 돌봄의 연결','용기를 꺼내기 전에 공급 차단, 남은 물을 받을 곳, 뿌리·가지의 연결을 확인할 수 있어야 하는가? 청소·전정·교체를 한 사람의 실제 순서로 관찰한다. 장치가 만든 새 관리도 함께 센다.','관찰 질문',['REF-06']),
 card('lifetimes','서로 다른 수명','설치 기반, 식물, 용기, 펌프·센서·조명은 다른 주기로 바뀐다. 이사·식재 중단·고장 때 무엇을 유지할지 연구한다. 접점 규칙·부품 표기·설치 및 변경 기록·대체 부품을 설계 조건으로 본다.','장기 사용 제안',['ARC-03','ARC-05']),
 card('swot','SWOT에 더할 관점','강점 후보: 설치·수리·재구성의 연속성. 약점: 초기 설치와 관리 부품 증가. 기회 후보: 이사·돌봄·변경 서비스. 위협: 기존 모듈 식재 가구, 공급 중단, 독립 화분 선호. 비용 절감과 서비스 수요는 가설이다.','분석·수요 검증 전'),
 card('experiment','작은 수동 모형부터','프레임 하나에 식재 자리·빈 성장 구간·조명 또는 수납 하나를 구성한다. 추가·탈착·청소 접근·잠금 확인을 비교하고, 생육과 실제 설비는 별도 기록한다. 일반 선반이 같은 결과를 내는지도 비교한다.','첫 실험 제안'),
 card('decision','내가 결정할 빈칸','가져올 606 원리: ______\n조형 요소·첫 후보: ______\n오래 유지할 것 / 바꿀 것: ______\n직접 변경할 것 / 맡길 것: ______\n첫 적용 범위·보류 이유: ______','사용자 선택·미정')]}
]
if not any(s['id']=='arc_606' for s in d['sections']): d['sections'][3:3]=new
d['version']='0.3'
d['subtitle']=d['subtitle'].replace('v0.2','v0.3')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(base.parent/'new-reference-zones.json').write_text(json.dumps(new,ensure_ascii=False),encoding='utf-8')
cases=(base/'606_ARCHITECTURE_REFERENCES.md').read_text(encoding='utf-8')
for name in ['ANALYSIS.md','REPORT.md']:
 fp=base/name; text=fp.read_text(encoding='utf-8')
 if '# 설치하고 오래 쓰는 공간 인프라' not in text:
  text=text.replace('## 기존 집의 적용 연구 — 출발점과 감상',cases+'\n---\n\n## 기존 집의 적용 연구 — 출발점과 감상',1)
 text=text.replace('추가 조사 / v0.2','추가 조사 / v0.3')
 fp.write_text(text,encoding='utf-8')
print(json.dumps({'sections':len(d['sections']),'cards':sum(len(s['cards']) for s in d['sections']),'links':sum(len(c['sources']) for s in d['sections'] for c in s['cards']),'newZones':len(new)},ensure_ascii=False))
