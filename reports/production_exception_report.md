# Production KPI Monitoring and Exception Report

## Summary

- Production records analysed: 5
- Records requiring review: 1
- Total exceptions detected: 4

## Record-by-record results

### 2026-10-19

- Throughput: 25.00 tonnes
- Capacity utilisation: 50.00%
- DOC residual oil: 2.80%
- DOC moisture: 9.50%
- Solvent consumption: 200.00 L/t

**Status: No configured exceptions detected**

### 2026-10-20

- Throughput: 28.00 tonnes
- Capacity utilisation: 56.00%
- DOC residual oil: 2.40%
- DOC moisture: 10.20%
- Solvent consumption: 200.00 L/t

**Status: No configured exceptions detected**

### 2026-10-21

- Throughput: 22.00 tonnes
- Capacity utilisation: 44.00%
- DOC residual oil: 3.40%
- DOC moisture: 11.50%
- Solvent consumption: 268.18 L/t

**Status: REVIEW REQUIRED**

Exceptions:
- HIGH DOC RESIDUAL OIL
- HIGH DOC MOISTURE
- HIGH SOLVENT CONSUMPTION
- LOW CAPACITY UTILIZATION

Investigation guidance:

### HIGH DOC RESIDUAL OIL

- Why it matters: High residual oil in de-oiled cake may indicate that extraction performance needs investigation.
- Suggested checks:
  - Verify the laboratory result and sampling method.
  - Review solvent-to-feed ratio and solvent distribution.
  - Check feed preparation and material condition.
  - Review extractor operating conditions.
- Note: This is an investigation guide, not a confirmed root cause. Thresholds are provisional and require operational validation.

### HIGH DOC MOISTURE

- Why it matters: High de-oiled cake moisture may affect product quality, storage stability, and downstream handling.
- Suggested checks:
  - Verify the moisture result and sampling method.
  - Review desolventizer-toaster operating conditions.
  - Check drying performance and relevant temperature readings.
  - Review steam supply and material residence time.
- Note: This is an investigation guide, not a confirmed root cause. Thresholds are provisional and require operational validation.

### HIGH SOLVENT CONSUMPTION

- Why it matters: High solvent consumption per tonne may increase operating costs and warrants investigation of solvent usage and recovery.
- Suggested checks:
  - Verify solvent usage and throughput measurements.
  - Review solvent inventory and tank-level records.
  - Check for leaks or unexplained solvent losses.
  - Review solvent recovery system performance.
- Note: This is an investigation guide, not a confirmed root cause. Thresholds are provisional and require operational validation.

### LOW CAPACITY UTILIZATION

- Why it matters: Low capacity utilization means recorded throughput is below half of the configured rated daily capacity.
- Suggested checks:
  - Verify the plant's rated daily capacity.
  - Review feed availability and feed quality.
  - Check operating hours, downtime, and stoppages.
  - Investigate equipment bottlenecks and process constraints.
- Note: This is an investigation guide, not a confirmed root cause. Thresholds are provisional and require operational validation.

### 2026-10-22

- Throughput: 30.00 tonnes
- Capacity utilisation: 60.00%
- DOC residual oil: 2.10%
- DOC moisture: 9.00%
- Solvent consumption: 180.00 L/t

**Status: No configured exceptions detected**

### 2026-10-23

- Throughput: 26.00 tonnes
- Capacity utilisation: 52.00%
- DOC residual oil: 2.60%
- DOC moisture: 10.00%
- Solvent consumption: 200.00 L/t

**Status: No configured exceptions detected**

## Important limitations

- This report supports investigation; it does not diagnose root causes.
- Default thresholds are provisional and require plant validation.
- Verify flagged readings against reliable operating records.
- No alert does not guarantee that a process is safe or optimal.
- The sample data is illustrative, not verified plant performance.

