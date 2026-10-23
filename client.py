# -*- coding: utf-8 -*-
"""Freight Damage Carmack Claim Compiler for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class FreightDamageCarmackClaimCompiler:
    @staticmethod
    def evaluate_carmack_liability_prima_facie(has_clean_bol_origin: bool, has_delivery_receipt_exception: bool, cargo_invoice_value_usd: float, salvage_recovered_usd: float = 0.0) -> Dict[str, Any]:
        prima_facie_established = has_clean_bol_origin and has_delivery_receipt_exception
        net_claim_usd = round(max(0.0, cargo_invoice_value_usd - salvage_recovered_usd), 2)
        
        status = "PRIMA_FACIE_CARRIER_LIABILITY_ESTABLISHED" if prima_facie_established else "CONCEALED_DAMAGE_BURDEN_OF_PROOF"
        return {
            "clean_bol_proven": has_clean_bol_origin,
            "exception_noted_at_delivery": has_delivery_receipt_exception,
            "total_cargo_loss_usd": net_claim_usd,
            "legal_standing": status,
            "governing_law": "Carmack Amendment (49 U.S.C. § 14706)",
            "burden_of_proof": "Burden shifts entirely to carrier to prove common carrier defense (Act of God, public enemy, shipper default)." if prima_facie_established else "Shipper must provide time-stamped uncrating inspection within 5 business days."
        }

    @staticmethod
    def generate_carmack_freight_claim_notice(carrier_scac: str, pro_number: str, loss_amount_usd: float, damage_description: str = "Crushed pallets and broken internal packaging") -> Dict[str, Any]:
        memo = f"""FORMAL PRESENTATION OF FREIGHT CLAIM (49 C.F.R. § 1005)

To: Claims Department, Carrier SCAC [{carrier_scac}]
PRO Tracking Number: {pro_number}
Claimed Loss: ${loss_amount_usd:.2f}

Demand is hereby formally made for cargo loss/damage sustained in transit: {damage_description}.
Clean Bill of Lading and Delivery Exception Receipt are attached.

In accordance with 49 C.F.R. § 1005.3, you are required to acknowledge receipt of this claim within 30 days and pay, decline, or settle within 120 days.
"""
        return {
            "pro_number": pro_number,
            "carrier_scac": carrier_scac,
            "claimed_total_usd": loss_amount_usd,
            "formal_claim_document": memo,
            "statutory_filing_deadline_days": 270
        }
