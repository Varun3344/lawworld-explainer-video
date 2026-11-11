"""Build ~/Downloads/LawWorld_Judgment_Reels_Tracker.xlsx (daily log of judgment reels: date, court, judgment, video link, posts)."""
import datetime as dt, os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.expanduser("~/Downloads/LawWorld_Judgment_Reels_Tracker.xlsx")

# file name -> final video link (matched by exact byte size to the delivered file)
links = {}
for line in open(os.path.join(SP, "stem_url.txt")):
    f, u = line.strip().split("|")
    links[f] = u
links["KHC_CrlP_13177_2026_Naveen_24_hour_clock_from_detention_9x16.mp4"] = \
    "https://videos.lawworld.ai/reels/concept/naveen-v-state-of-karnataka-2026-khc-60797/final-9x16-20261104-053430Z.mp4"

D4 = dt.date(2026, 11, 4)
FB, IG = "https://www.facebook.com/reel/", "https://www.instagram.com/"
# (court, judgment, case no / citation, judgment date, language, point, file, fb, ig, posted on)
R = [
 ("Supreme Court", "N. Sridhar Reddy v. State of A.P. & Ors.", "2026 INSC 1191 (Crl.A. 5187/2026)", "03-11-2026", "English", "A UK divorce is no shield from a bigamy case", "SC_SridharReddy_2026INSC1191_UK_divorce_no_shield_from_bigamy_case_9x16.mp4"),
 ("Supreme Court", "Surendra Manjhi & Anr. v. Union of India & Ors.", "2026 INSC 1185 (W.P.(C) 511/2022)", "02-11-2026", "English", "Rescued bonded labourers get aid within 7 days", "SC_SurendraManjhi_2026INSC1185_bonded_labour_aid_within_7_days_9x16.mp4"),
 ("Supreme Court", "Bandari Ramchander & Ors. v. Maitri Coop. Housing Society Ltd. & Ors.", "2026 INSC 1175 (C.A. 10699/2013)", "29-10-2026", "English", "A jagir grant is not ownership (Miyapur land)", "SC_BandariRamchander_2026INSC1175_jagir_not_ownership_Miyapur_9x16.mp4"),
 ("Supreme Court", "In Re: A Judicial Officer, Rajasthan Judicial Services", "2026 INSC 1188 (SLP(Crl.) 13501/2025)", "02-11-2026", "English", "No strictures against a judge without a hearing", "SC_InRe_JudicialOfficer_2026INSC1188_no_strictures_without_hearing_9x16.mp4"),
 ("Supreme Court", "Goverdhan v. State of Rajasthan", "2026 INSC 1190 (Crl.A. 1394/2017)", "03-11-2026", "English", "Abetment: letters not proved, accused acquitted", "SC_Goverdhan_2026INSC1190_abetment_letters_unproved_acquitted_9x16.mp4"),
 ("Supreme Court", "Mangala Bhimrao Ingle v. Addl. Commissioner, Amravati Division & Ors.", "2026 INSC 1193 (SLP(C) 30772/2025)", "04-11-2026", "English", "Two-child norm sent to a larger bench; Sarpanch continues", "SC_MangalaIngle_2026INSC1193_two_child_norm_referred_larger_bench_9x16.mp4",
  FB + "901019556335305/", IG + "lawworld.supremecourt/reel/DfWHTCAg56W/", "05-11-2026"),
 ("Karnataka HC", "Naveen v. State of Karnataka", "2026:KHC:60797 (Crl.P. 13177/2026)", "02-11-2026", "English", "24-hour rule runs from actual detention", "KHC_CrlP_13177_2026_Naveen_24_hour_clock_from_detention_9x16.mp4",
  FB + "28890803457267417/", IG + "lawworld.highcourts/reel/DfTuo7qqNWD/", "04-11-2026"),
 ("Karnataka HC", "Suo Motu PIL: safety of Advocates (Karnataka High Court)", "Suo motu PIL, oral order", "03-11-2026", "English", "Court takes up advocates' safety; hearing 8 December", "KHC_SuoMotu_PIL_Advocates_safety_03_11_2026_English_9x16.mp4",
  FB + "1146131027790048/", IG + "lawworld.highcourts/reel/DfWGP0Cq3-V/", "05-11-2026"),
 ("Karnataka HC", "Suo Motu PIL: safety of Advocates (Karnataka High Court)", "Suo motu PIL, oral order", "03-11-2026", "Kannada", "Same order, Kannada version", "KHC_SuoMotu_PIL_Advocates_safety_03_11_2026_Kannada_9x16.mp4"),
 ("Karnataka HC", "Sri Sridhara Babu v. Karnataka State Financial Corporation & Ors.", "2026:KHC:59867-DB (COMAP 446/2026)", "28-10-2026", "English", "Guarantor's heirs liable only up to the estate", "KHC_COMAP_446_2026_KSFC_guarantor_heirs_liable_only_to_estate_9x16.mp4"),
 ("Karnataka HC", "Shiva Enterprises & Ors. v. State of Maharashtra & Ors.", "2026:KHC:60505 (W.P. 31910/2025)", "29-10-2026", "English", "Maharashtra police notices not enforceable", "KHC_WP_31910_2025_Maharashtra_police_notices_unenforceable_9x16.mp4"),
 ("Karnataka HC", "Divisional Controller, KKRTC v. Smt. Mantavva & Anr.", "2026:KHC-D:17610-DB (W.A. 100758/2025)", "28-10-2026", "English", "Brother gets no compassionate appointment", "KHC_WA_100758_2025_KKRTC_brother_no_compassionate_job_9x16.mp4"),
 ("Karnataka HC", "CESCOM v. J.K. Tyre and Industries Ltd. & Anr.", "W.A. 439/2025", "29-10-2026", "English", "Lockdown-period demand charges are payable", "KHC_WA_439_2025_CESCOM_lockdown_demand_charges_payable_9x16.mp4"),
 ("Karnataka HC", "Shanker Mahadevan Iyer v. Deputy Director, Enforcement Directorate", "2026:KHC:59898 (W.P. 34513/2024)", "28-10-2026", "English", "ED can attach property bought before the crime", "KHC_WP_34513_2024_ED_can_attach_property_bought_before_crime_9x16.mp4"),
 ("Karnataka HC", "Renuka Ramnath v. State of Karnataka (Legal Metrology)", "2026:KHC:59939 (W.P. 18251/2021)", "28-10-2026", "English", "Non-executive director: Legal Metrology case quashed", "KHC_WP_18251_2021_non_executive_director_Legal_Metrology_quashed_9x16.mp4"),
 ("Madras HC", "M/s. Jaison Electronics v. Mujahid Baig & Anr.", "2026:MHC:4386 (C.R.P. 1837/2026)", "30-10-2026", "English", "No tenancy agreement: eviction stands", "MAD_CRP_1837_2026_no_tenancy_agreement_eviction_stands_9x16.mp4"),
 ("Madras HC", "S.R. Balakrishnan v. State of Tamil Nadu & Ors.", "2026:MHC:4344 (W.P. 27070/2024 batch)", "28-10-2026", "English", "MGNREGS computer assistants to be absorbed", "MAD_WP_27070_2024_MGNREGS_computer_assistants_to_be_absorbed_9x16.mp4"),
 ("Madras HC", "Secretary, MAWS Dept., Govt. of Tamil Nadu v. Waste Management Operators Assn.", "2026:MHC:4432 (W.A. 3362/2026)", "03-11-2026", "English", "Stay on the waste-management G.O. lifted", "MAD_WA_3362_2026_waste_management_GO_stay_lifted_9x16.mp4"),
 ("Madras HC", "Lourde Marie Dhambarane & Anr. v. S. Santhi", "2026:MHC:4366 (C.R.P. 1196/2022)", "29-10-2026", "English", "Buyer's suit struck off as abuse of process", "MAD_CRP_1196_2022_buyer_suit_struck_off_abuse_of_process_9x16.mp4"),
 ("Madras HC", "Royal Sundaram General Insurance Co. Ltd. v. Asaraf Asad & Ors.", "C.M.A.(MD) 627/2024 (Madurai Bench)", "02-11-2026", "English", "Injured driver's employee compensation upheld", "MAD_CMAMD_627_2024_injured_driver_employee_compensation_upheld_9x16.mp4"),
 ("Madras HC", "Reha Environ Pvt. Ltd. & Anr. v. Government of Puducherry & Ors.", "2026:MHC:4381 (C.R.P. 5394/2026 batch)", "30-10-2026", "English", "Puducherry Government bound by the arbitral award", "MAD_CRP_5394_2026_Puducherry_govt_bound_by_arbitral_award_9x16.mp4"),
 ("Delhi HC", "Adit Buildwell Pvt. Ltd. v. Commissioner of CGST, South Commissionerate & Anr.", "W.P.(C) 2728/2024", "29-10-2026", "English", "Request for time ignored: tax order set aside", "Delhi_WPC_2728_2024_AditBuildwell_time_request_ignored_order_set_aside_9x16.mp4"),
 ("Delhi HC", "Chief Electoral Officer & Anr. v. M/s Mahlakshmi Light House", "FAO(OS)(COMM) 43/2018", "28-10-2026", "English", "Election tent contractor's award stands", "Delhi_FAOOSCOMM_43_2018_election_tent_contractor_award_stands_9x16.mp4"),
 ("Delhi HC", "C R Sons Infra Projects Ltd v. IRCON International Ltd", "FAO(OS)(COMM) 60/2019", "29-10-2026", "English", "Arbitrator went beyond the dispute", "Delhi_FAOOSCOMM_60_2019_CRSons_v_IRCON_arbitrator_beyond_dispute_9x16.mp4"),
 ("Delhi HC", "MMTC Limited v. Aust Grain Exports Pty Ltd", "FAO(OS)(COMM) 210/2023", "28-10-2026", "English", "Interest on the guarantee set aside", "Delhi_FAOOSCOMM_210_2023_MMTC_guarantee_interest_set_aside_9x16.mp4"),
 ("Kerala HC", "Mohammad Irfan K.I. v. State Bank of India & Ors.", "2026:KER:82568 (W.A. 2209/2026)", "28-10-2026", "English", "Bank credits alone don't justify a court-ordered probe", "Kerala_WA_2209_2026_bank_credits_alone_no_court_ordered_probe_9x16.mp4"),
 ("Kerala HC", "Mary Victoria v. Ministry of External Affairs & Ors.", "WP(C) 35189/2025 (interim order)", "28-10-2026", "English", "Dignified burial: interim directions", "Kerala_WPC_35189_2025_dignified_burial_interim_order_9x16.mp4"),
 ("Telangana HC", "Uday Chand Vedi v. Puneet Vedi", "C.C.C.A. 68/2010", "30-10-2026", "English", "Token advance: sale decree set aside", "TG_CCCA_68_2010_token_advance_sale_decree_set_aside_9x16.mp4"),
 ("Telangana HC", "Sri Jakkula Dasharatham & Ors. v. Sri Jakkula Balaiah & Ors.", "C.R.P. 6423/2012", "28-10-2026", "English", "Protected-tenant certificate goes to all heirs", "TG_CRP_6423_2012_protected_tenant_certificate_to_all_heirs_9x16.mp4"),
 ("Andhra Pradesh HC", "Anisha Busa v. SIBAR Institute of Dental Sciences & Anr.", "2026:APHC:46012 (W.P. 15274/2020)", "28-10-2026", "English", "College cannot keep original certificates", "AP_WP_15274_2020_college_cannot_keep_original_certificates_9x16.mp4"),
 ("Andhra Pradesh HC", "Paravada Ganesh & Ors. v. State of Andhra Pradesh & Ors.", "2026:APHC:47018 (W.P. 27611/2025 batch)", "30-10-2026", "English", "Constable recruitment: no-waiting-list clause arbitrary", "AP_WP_27611_2025_constable_no_waiting_list_clause_arbitrary_9x16.mp4"),
 ("Andhra Pradesh HC", "National Insurance Co. Ltd. v. Bammidi Savithri & Ors.", "2026:APHC:46786 (M.A.C.M.A. 3096/2017)", "02-11-2026", "English", "Insurer's appeal: compensation raised", "AP_MACMA_3096_2017_insurer_appeal_award_raised_9x16.mp4"),
 ("Andhra Pradesh HC", "Perumalla Kasi Rao v. Nukala Muralikrishna & Ors.", "2026:APHC:47171 (A.S. 82/2013 batch)", "03-11-2026", "English", "Plaint wrongly rejected: suits go to trial", "AP_AS_82_2013_plaint_wrongly_rejected_suit_to_trial_9x16.mp4"),
]

def d(s):
    return dt.datetime.strptime(s, "%d-%m-%Y").date()

ARIAL = "Arial"
HEAD_FILL = PatternFill("solid", fgColor="3B2A20")
BAND_FILL = PatternFill("solid", fgColor="F6EFE6")
thin = Side(style="thin", color="D9CFC3")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
HF = Font(name=ARIAL, bold=True, color="FFFFFF", size=10)
BF = Font(name=ARIAL, size=10)
LF = Font(name=ARIAL, size=10, color="0563C1", underline="single")

wb = Workbook()
ws = wb.active
ws.title = "Reels"
heads = ["Date created", "No.", "Court", "Judgment", "Case no. / Citation", "Judgment date", "Language",
         "What the reel says", "Video link", "Facebook post", "Instagram post", "Posted on", "File name (Downloads)"]
ws.append(heads)
for c in range(1, len(heads) + 1):
    cell = ws.cell(row=1, column=c); cell.font = HF; cell.fill = HEAD_FILL
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True); cell.border = BORDER
ws.row_dimensions[1].height = 30

missing = []
for i, r in enumerate(R, start=1):
    court, judg, cite, jdate, lang, point, fname = r[:7]
    fb, ig, posted = (r[7], r[8], r[9]) if len(r) > 7 else ("", "", "")
    url = links.get(fname)
    if not url:
        missing.append(fname)
    row = 1 + i
    vals = [D4, i, court, judg, cite, d(jdate), lang, point, url, fb or None, ig or None, d(posted) if posted else None, fname]
    for c, v in enumerate(vals, start=1):
        cell = ws.cell(row=row, column=c, value=v)
        cell.font = BF; cell.border = BORDER
        cell.alignment = Alignment(vertical="top", wrap_text=c in (4, 5, 8))
        if i % 2 == 0:
            cell.fill = BAND_FILL
    ws.cell(row=row, column=1).number_format = "DD-MM-YYYY"
    ws.cell(row=row, column=6).number_format = "DD-MM-YYYY"
    ws.cell(row=row, column=12).number_format = "DD-MM-YYYY"
    ws.cell(row=row, column=2).alignment = Alignment(horizontal="center", vertical="top")
    for c, label in ((9, "Watch video"), (10, "Facebook"), (11, "Instagram")):
        cell = ws.cell(row=row, column=c)
        if cell.value:
            cell.hyperlink = cell.value; cell.value = label; cell.font = LF
if missing:
    sys.exit("missing links: %s" % missing)

widths = [12, 5, 16, 44, 30, 12, 9, 40, 13, 11, 11, 11, 58]
for c, w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(c)].width = w
ws.freeze_panes = "D2"
last = 1 + len(R)
ws.auto_filter.ref = "A1:M%d" % last

# ---- Daily summary (formulas over the Reels sheet) ----
sm = wb.create_sheet("Daily Summary", 0)
sm["A1"] = "LawWorld judgment reels: daily count"
sm["A1"].font = Font(name=ARIAL, bold=True, size=14, color="3B2A20")
sm["A2"] = ("One row per day. Counts come from the Reels sheet automatically. New reels are added to the Reels sheet "
            "with the date they were made. 04-11-2026's batch (33 reels) was finished overnight; the last one was "
            "completed at 07:42 on 05-11-2026.")
sm["A2"].font = Font(name=ARIAL, size=9, italic=True, color="6B5B4F")
sm["A2"].alignment = Alignment(wrap_text=True, vertical="top")
sm.merge_cells("A2:F2"); sm.row_dimensions[2].height = 42
sh = ["Date", "Judgment reels created", "Supreme Court", "High Courts", "Posted on social media", "Not posted yet"]
for c, h in enumerate(sh, start=1):
    cell = sm.cell(row=4, column=c, value=h); cell.font = HF; cell.fill = HEAD_FILL; cell.border = BORDER
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
sm.row_dimensions[4].height = 30
days = [D4, dt.date(2026, 11, 5)]
rng = "Reels!$A$2:$A$1000"
for k, day in enumerate(days):
    r = 5 + k
    sm.cell(row=r, column=1, value=day).number_format = "DD-MM-YYYY"
    sm.cell(row=r, column=2, value="=COUNTIF(%s,A%d)" % (rng, r))
    sm.cell(row=r, column=3, value='=COUNTIFS(%s,A%d,Reels!$C$2:$C$1000,"Supreme Court")' % (rng, r))
    sm.cell(row=r, column=4, value="=B%d-C%d" % (r, r))
    sm.cell(row=r, column=5, value='=COUNTIFS(%s,A%d,Reels!$L$2:$L$1000,"<>")' % (rng, r))
    sm.cell(row=r, column=6, value="=B%d-E%d" % (r, r))
    for c in range(1, 7):
        cell = sm.cell(row=r, column=c); cell.font = BF; cell.border = BORDER
        cell.alignment = Alignment(horizontal="center")
tr = 5 + len(days)
sm.cell(row=tr, column=1, value="Total")
for c in range(2, 7):
    col = get_column_letter(c)
    sm.cell(row=tr, column=c, value="=SUM(%s5:%s%d)" % (col, col, tr - 1))
for c in range(1, 7):
    cell = sm.cell(row=tr, column=c); cell.font = Font(name=ARIAL, bold=True, size=10); cell.border = BORDER
    cell.alignment = Alignment(horizontal="center"); cell.fill = BAND_FILL
for c, w in enumerate([14, 22, 15, 14, 22, 15], start=1):
    sm.column_dimensions[get_column_letter(c)].width = w

wb.calculation.fullCalcOnLoad = True
wb.save(OUT)
print("saved", OUT, "rows", len(R))
# expected values for a check
for day in days:
    rows = [r for r in R if D4 == day]
    sc = sum(1 for r in rows if r[0] == "Supreme Court")
    posted = sum(1 for r in rows if len(r) > 7)
    print(day, "created", len(rows), "SC", sc, "HC", len(rows) - sc, "posted", posted)
