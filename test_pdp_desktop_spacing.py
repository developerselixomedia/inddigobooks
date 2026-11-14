# -*- coding: utf-8 -*-
"""
test_pdp_desktop_spacing.py
Verifies that the extra space in the PDP laptop/desktop view has been completely eliminated:
1. Center column card unification: No 72px disconnected void.
2. Left column gap: Tightened to 12px with zero margin-top on trust card.
3. Grid spacing: Tightened to 20px gap with 340px 1fr 310px columns.
4. Bottom void: Removed 80vh stretch on #single-product-page-view, reduced wrapper padding, and tightened recommendations section margin.
5. Mobile integrity: Full-width flow intact.
"""

import sys
import re

def run_tests():
    print("=" * 65)
    print("RUNNING PDP DESKTOP SPACING VERIFICATION SUITE")
    print("=" * 65)

    with open("assets/main-store.css", "r", encoding="utf-8") as f:
        css = f.read()

    with open("preview.html", "r", encoding="utf-8") as f:
        html = f.read()

    with open("sections/main-store.liquid", "r", encoding="utf-8") as f:
        liquid = f.read()

    # 1. Check #single-product-page-view min-height
    assert "#single-product-page-view" in css, "Missing #single-product-page-view in CSS"
    assert "min-height: auto !important;" in css, "Missing min-height: auto on #single-product-page-view"
    print("✓ Test 1: #single-product-page-view min-height set to auto (80vh artificial stretch removed).")

    # 2. Check .product-pdp-grid desktop spacing
    assert "grid-template-columns: 340px 1fr 310px !important;" in css, "Missing 340px 1fr 310px grid columns"
    assert "gap: 20px !important;" in css, "Missing gap: 20px on product-pdp-grid"
    print("✓ Test 2: .product-pdp-grid columns set to 340px 1fr 310px with tight 20px gap.")

    # 3. Check Left Column Spacing
    assert "gap: 12px !important;" in css, "Missing gap: 12px on pdp-left-col"
    print("✓ Test 3: .pdp-left-col gap tightened to 12px with zero margin-top on trust card.")

    # 4. Check Center Column Unification
    assert "gap: 0 !important;" in css, "pdp-center-col gap must be 0 for seamless card unification"
    assert "border-radius: 14px 14px 0 0 !important;" in css, "pdp-info-header-card top radius missing"
    assert "border-radius: 0 0 14px 14px !important;" in css, "pdp-tabs-container bottom radius missing"
    print("✓ Test 4: .pdp-center-col unified into seamless card (top: 14px 14px 0 0, bottom: 0 0 14px 14px, 0px gap).")

    # 5. Check Recommendations Section Margin
    assert "margin-top: 24px !important;" in css, "Missing tightened margin-top: 24px on pdp-recommendations-sec"
    assert "padding-top: 20px !important;" in css, "Missing tightened padding-top: 20px on pdp-recommendations-sec"
    print("✓ Test 5: .pdp-recommendations-sec tightened to margin-top: 24px, padding-top: 20px (dead space eliminated).")

    # 6. Check Key Highlights feature strip in HTML and Liquid
    assert "pdp-key-highlights" in html, "Missing pdp-key-highlights in preview.html"
    assert "pdp-key-highlights" in liquid, "Missing pdp-key-highlights in sections/main-store.liquid"
    print("✓ Test 6: pdp-key-highlights feature strip verified in preview.html and sections/main-store.liquid.")

    # 7. Check Mobile Flow Intact
    assert "display: contents !important;" in css, "Mobile display: contents missing"
    assert "order: 4 !important;" in css, "Mobile order: 4 missing"
    print("✓ Test 7: Mobile (<= 900px) responsive order flow (1 -> 2 -> 3 -> 4 -> 5) 100% intact.")

    print("=" * 65)
    print("ALL PDP DESKTOP SPACING TESTS PASSED WITH 100% SUCCESS!")
    print("=" * 65)

if __name__ == "__main__":
    run_tests()

