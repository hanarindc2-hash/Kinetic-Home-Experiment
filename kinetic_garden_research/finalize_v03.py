from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from hashlib import sha256
import json
from pypdf import PdfReader

base = Path(__file__).resolve().parent / 'kinetic-garden'
docx = base / 'Living_Spatial_Infrastructure_Prologue_and_606_v0.3.docx'
pdf = base.parent / 'docx-qa/verified-pages' / (docx.stem + '.pdf')
verification = json.loads((base / 'DOCX_VERIFICATION.json').read_text(encoding='utf-8'))
reader = PdfReader(pdf)
text = '\n'.join(page.extract_text() or '' for page in reader.pages)
assert len(reader.pages) == 25
assert '\ufffd' not in text
assert all(name in text for name in ['USM', 'Habraken', 'Bosch', 'GARDENA', 'Neutrik', '606'])
verification.update({
    'renderStatus': 'verified',
    'checkedAt': '2026-10-11',
    'renderedPages': len(reader.pages),
    'renderer': 'Canonical render_docx.py with workspace-only LibreOffice 26.8.1 and Poppler',
    'visualInspection': 'All 25 rendered pages inspected; tables, Korean glyphs, source links, and decision paragraphs checked. Pages 13 and 17 additionally inspected at 180 DPI.',
    'docxSha256': sha256(docx.read_bytes()).hexdigest(),
    'renderedPdfSha256': sha256(pdf.read_bytes()).hexdigest(),
    'wordNativeVerification': False,
    'editable': 'Native Word paragraphs, heading styles, tables, hyperlinks, and blank decision records',
    'researchBoundary': 'Published-source research and design hypotheses; physical prototype, demand, plant growth, installation, and regulatory suitability not verified'
})
(base / 'DOCX_VERIFICATION.json').write_text(json.dumps(verification, ensure_ascii=False, indent=2), encoding='utf-8')
readme = (base / 'README.md').read_text(encoding='utf-8')
anchor = '로컬 플러그인은 구문, 전체 데이터 형식, 수정본 내보내기 모의 검사를 통과했습니다.'
addition = 'DOCX는 LibreOffice로 실제 25쪽으로 변환해 모든 페이지의 글꼴·표·페이지 나눔을 시각적으로 확인했습니다. Microsoft Word에서 직접 열어 확인한 결과는 아닙니다. 본문·표·출처 링크·선택 기록은 편집 가능한 요소입니다.\n\n'
if addition.strip() not in readme:
    readme = readme.replace(anchor, addition + anchor)
(base / 'README.md').write_text(readme, encoding='utf-8')
board_verification = json.loads((base / 'VERIFICATION.json').read_text(encoding='utf-8'))
board_verification['docxStatus'] = {'renderedPages': 25, 'allPagesVisuallyInspected': True, 'wordNativeVerification': False}
(base / 'VERIFICATION.json').write_text(json.dumps(board_verification, ensure_ascii=False, indent=2), encoding='utf-8')
files = sorted(p for p in base.iterdir() if p.is_file() and p.suffix.lower() in {'.md', '.json', '.docx', '.png'})
files += [base / 'plugin' / name for name in ['code.js', 'ui.html', 'manifest.json', 'README.md']]
assert all(p.is_file() for p in files)
package = base.parent / 'Kinetic_Garden_Research_v0.3.zip'
with ZipFile(package, 'w', ZIP_DEFLATED) as z:
    for p in files:
        z.write(p, Path('kinetic-garden') / p.relative_to(base))
with ZipFile(package) as z:
    assert z.testzip() is None
    assert any(name.endswith('.docx') for name in z.namelist())
print(json.dumps({'docxPages':25, 'packageFiles':len(files), 'package':str(package), 'bytes':package.stat().st_size, 'docxSha256':verification['docxSha256']}, ensure_ascii=False))
