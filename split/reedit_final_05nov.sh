#!/bin/zsh
# 05-11-2026 01:50: ONE re-edit pass (edit + final + qa + ship) over every delivered reel, with the final split-switch fix (switch stays
# before the c01/c02 seam, panel held blank until the hook card's tail is gone). Replaces the earlier re-edit runners. apk keeps the Kannada font.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
typeset -A STEM SLUG
STEM=(ukd SC_SridharReddy_2026INSC1191_UK_divorce_no_shield_from_bigamy_case bnd SC_SurendraManjhi_2026INSC1185_bonded_labour_aid_within_7_days
 hgd KHC_COMAP_446_2026_KSFC_guarantor_heirs_liable_only_to_estate mhr KHC_WP_31910_2025_Maharashtra_police_notices_unenforceable
 rnt MAD_CRP_1837_2026_no_tenancy_agreement_eviction_stands mgn MAD_WP_27070_2024_MGNREGS_computer_assistants_to_be_absorbed
 bac Kerala_WA_2209_2026_bank_credits_alone_no_court_ordered_probe bur Kerala_WPC_35189_2025_dignified_burial_interim_order
 adt Delhi_WPC_2728_2024_AditBuildwell_time_request_ignored_order_set_aside elt Delhi_FAOOSCOMM_43_2018_election_tent_contractor_award_stands
 tka TG_CCCA_68_2010_token_advance_sale_decree_set_aside ptn TG_CRP_6423_2012_protected_tenant_certificate_to_all_heirs
 crt AP_WP_15274_2020_college_cannot_keep_original_certificates pcw AP_WP_27611_2025_constable_no_waiting_list_clause_arbitrary)
SLUG=(ukd sridhar-reddy-v-state-of-ap-2026-insc-1191 bnd surendra-manjhi-v-union-of-india-2026-insc-1185 hgd sridhara-babu-v-ksfc-2026-khc-59867
 mhr shiva-enterprises-v-state-of-maharashtra-2026-khc-60505 rnt jaison-electronics-v-mujahid-baig-2026-mhc-4386 mgn sr-balakrishnan-v-state-of-tn-2026-mhc-4344
 bac mohammad-irfan-v-sbi-2026-ker-82568 bur mary-victoria-v-mea-kerala-hc-interim-order-28-10-2026 adt adit-buildwell-v-cgst-delhi-south-dhc-29-10-2026
 elt chief-electoral-officer-v-mahlakshmi-light-house-dhc-28-10-2026 tka uday-chand-vedi-v-puneet-vedi-tshc-30-10-2026
 ptn jakkula-dasharatham-v-jakkula-balaiah-tshc-28-10-2026 crt sibar-dental-college-certificates-2026-aphc-46012 pcw paravada-ganesh-v-state-of-ap-2026-aphc-47018)
STEM[ape]=KHC_SuoMotu_PIL_Advocates_safety_03_11_2026_English; SLUG[ape]=suo-motu-pil-advocates-safety-khc-03-11-2026-english
STEM[apk]=KHC_SuoMotu_PIL_Advocates_safety_03_11_2026_Kannada; SLUG[apk]=suo-motu-pil-advocates-safety-khc-03-11-2026-kannada
STEM[jdo]=SC_InRe_JudicialOfficer_2026INSC1188_no_strictures_without_hearing; SLUG[jdo]=in-re-judicial-officer-rajasthan-2026-insc-1188
heavy() { echo $(( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') + $(pgrep -f "build_vertical_course.py [a-z0-9]+ final" | wc -l | tr -d ' ') )); }
for s in ape apk bur jdo ukd elt tka hgd mgn adt rnt bac pcw ptn bnd mhr crt; do
  [ $s = crt ] && until grep -q "crt SHIPPED\|crt SHIP FAILED\|crt POST FAILED" logs/priority_05nov.log 2>/dev/null; do sleep 30; done
  while (( $(heavy) >= 4 )); do sleep 30; done
  echo "$(date +%H:%M:%S) $s re-edit start"
  if [ $s = apk ]; then export CAP_FONT="Kannada Sangam MN" QA_LANG=kn; else unset CAP_FONT QA_LANG; fi
  V_LAYOUT=judgment python3 split/build_vertical_course.py $s edit > logs/reedit3_$s.log 2>&1 && V_LAYOUT=judgment python3 split/build_vertical_course.py $s final >> logs/reedit3_$s.log 2>&1 || { echo "$(date +%H:%M:%S) $s RE-EDIT FAILED"; continue; }
  zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s ship ${SLUG[$s]} ${STEM[$s]} > logs/ship_$s.log 2>&1 && echo "$(date +%H:%M:%S) $s RESHIPPED edit=$(cat out/${s}9x16/edit.json) mask=$(cat out/${s}9x16/panel_mask.json)" || echo "$(date +%H:%M:%S) $s RESHIP FAILED"
done
echo "$(date +%H:%M:%S) RE-EDIT PASS DONE"
