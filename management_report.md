# Manufacturing Performance Management Report

## 1. Purpose

This report analyzes synthetic manufacturing data using Python-calculated KPIs, provisional exception rules, and a rule-based explanation engine.

The explanations suggest areas for investigation. They do not identify confirmed root causes.

## 2. Overall Summary

- Production records analyzed: 5
- Average throughput: 26.20 tonnes/day
- Average capacity utilization: 52.40%
- Average daily solvent consumption rate: 209.64 L/tonne
- Records requiring review: 1
- Total exceptions detected: 4

## 3. Daily Findings

| Date | Throughput (t) | Utilization (%) | DOC residual oil (%) | DOC moisture (%) | Solvent (L/t) | Status |
|---|---:|---:|---:|---:|---:|---|
| 2026-10-19 | 25.00 | 50.00 | 2.80 | 9.50 | 200.00 | No exception detected |
| 2026-10-20 | 28.00 | 56.00 | 2.40 | 10.20 | 200.00 | No exception detected |
| 2026-10-21 | 22.00 | 44.00 | 3.40 | 11.50 | 268.18 | REVIEW REQUIRED |
| 2026-10-22 | 30.00 | 60.00 | 2.10 | 9.00 | 180.00 | No exception detected |
| 2026-10-23 | 26.00 | 52.00 | 2.60 | 10.00 | 200.00 | No exception detected |

## 4. Exceptions Requiring Review

### 2026-10-21

**Throughput:** 22.00 tonnes

- HIGH DOC RESIDUAL OIL
- HIGH DOC MOISTURE
- HIGH SOLVENT CONSUMPTION
- LOW CAPACITY UTILIZATION

## 5. Explanations and Recommended Investigations

### 2026-10-21

#### HIGH DOC RESIDUAL OIL

- **Observed value:** 3.40%
- **Provisional threshold:** above 3.00%
- **Why it matters:** High residual oil in de-oiled cake may indicate that extraction performance needs investigation.

**Suggested investigation:**

- Verify the laboratory result and sampling method.
- Review solvent-to-feed ratio and solvent distribution.
- Check feed preparation and material condition.
- Review extractor operating conditions.

> **Caution:** This is an investigation guide, not a confirmed root cause. Thresholds are provisional and require operational validation.

#### HIGH DOC MOISTURE

- **Observed value:** 11.50%
- **Provisional threshold:** above 11.00%
- **Why it matters:** High de-oiled cake moisture may affect product quality, storage stability, and downstream handling.

**Suggested investigation:**

- Verify the moisture result and sampling method.
- Review desolventizer-toaster operating conditions.
- Check drying performance and relevant temperature readings.
- Review steam supply and material residence time.

> **Caution:** This is an investigation guide, not a confirmed root cause. Thresholds are provisional and require operational validation.

#### HIGH SOLVENT CONSUMPTION

- **Observed value:** 268.18L/tonne
- **Provisional threshold:** above 250.00L/tonne
- **Why it matters:** High solvent consumption per tonne may increase operating costs and warrants investigation of solvent usage and recovery.

**Suggested investigation:**

- Verify solvent usage and throughput measurements.
- Review solvent inventory and tank-level records.
- Check for leaks or unexplained solvent losses.
- Review solvent recovery system performance.

> **Caution:** This is an investigation guide, not a confirmed root cause. Thresholds are provisional and require operational validation.

#### LOW CAPACITY UTILIZATION

- **Observed value:** 44.00%
- **Provisional threshold:** below 50.00%
- **Why it matters:** Low capacity utilization means recorded throughput is below half of the configured rated daily capacity.

**Suggested investigation:**

- Verify the plant's rated daily capacity.
- Review feed availability and feed quality.
- Check operating hours, downtime, and stoppages.
- Investigate equipment bottlenecks and process constraints.

> **Caution:** This is an investigation guide, not a confirmed root cause. Thresholds are provisional and require operational validation.

## 6. Management Follow-up

- Verify flagged measurements and confirm data quality.
- Compare results with approved product specifications and validated operating limits.
- Review process records and investigate potential causes.
- Document findings and corrective actions after human review.
- Confirm any proposed operational change through the plant's approved procedures.

## 7. Limitations

All production data in this demonstration is synthetic. Thresholds are provisional examples, not approved plant limits. The explanations are rule-based investigation guidance, not AI-verified diagnoses or proof of process failure.

The report is not a substitute for plant procedures, qualified engineering judgment, or safety controls. Validate all thresholds, calculations, and recommendations before using real plant data.
