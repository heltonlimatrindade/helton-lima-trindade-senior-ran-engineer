# RAN KPI Reference Guide

## Key Performance Indicators (KPIs)

### Availability
**Definition**: Percentage of time a cell site or sector is operational and available to serve users.

**Formula**: `(Total Time - Downtime) / Total Time × 100`

**Industry Benchmark**: ≥ 99.5%

**Impact**: 
- Below 99%: Critical - Major service disruption
- 99-99.5%: Major - Noticeable service issues
- Above 99.5%: Good - Meets SLA requirements

**Common Causes of Low Availability**:
- Hardware failures
- Software crashes
- Power outages
- Transmission link failures
- Scheduled maintenance

---

### CSSR (Call Setup Success Rate)
**Definition**: Percentage of successful call setup attempts.

**Formula**: `(Successful RRC Connections / Total RRC Attempts) × 100`

**Industry Benchmark**: ≥ 98%

**Technologies**:
- **4G/5G**: RRC Connection Success Rate
- **3G**: RAB Setup Success Rate
- **2G**: TCH Assignment Success Rate

**Common Causes of Low CSSR**:
- Network congestion
- RF coverage issues
- Hardware capacity limits
- Configuration errors
- Interference

---

### DCR (Drop Call Rate)
**Definition**: Percentage of established calls that are dropped before normal termination.

**Formula**: `(Dropped Calls / Total Successful Calls) × 100`

**Industry Benchmark**: ≤ 2%

**Technologies**:
- **4G/5G**: E-RAB Drop Rate
- **3G**: RAB Drop Rate
- **2G**: TCH Drop Rate

**Common Causes of High DCR**:
- Poor RF coverage
- Handover failures
- Hardware issues
- Transmission problems
- Core network issues

---

### HOSR (Handover Success Rate)
**Definition**: Percentage of successful handover attempts between cells.

**Formula**: `(Successful Handovers / Total Handover Attempts) × 100`

**Industry Benchmark**: ≥ 98%

**Types**:
- **Intra-RAT**: Same technology (e.g., 4G to 4G)
- **Inter-RAT**: Different technology (e.g., 4G to 5G)
- **Intra-Frequency**: Same frequency band
- **Inter-Frequency**: Different frequency band

**Common Causes of Low HOSR**:
- Missing neighbour definitions
- Incorrect neighbour priorities
- RF coverage gaps
- Timing issues
- Parameter mismatches

---

### RRC Success Rate
**Definition**: Percentage of successful Radio Resource Control connection attempts.

**Formula**: `(RRC Connection Established / RRC Connection Attempts) × 100`

**Industry Benchmark**: ≥ 98.5%

**LTE/5G Specific**: First step in establishing data or voice connections

**Common Causes of Failures**:
- Network overload
- Poor uplink coverage
- Congestion control
- Access barring

---

### RSRP (Reference Signal Received Power)
**Definition**: Average power of LTE/5G reference signals received at the UE.

**Unit**: dBm

**Quality Levels**:
- **Excellent**: > -85 dBm
- **Good**: -85 to -100 dBm
- **Fair**: -100 to -110 dBm
- **Poor**: < -110 dBm

**Use Case**: 
- Cell selection and reselection
- Handover decisions
- Coverage analysis

---

### RSRQ (Reference Signal Received Quality)
**Definition**: Quality of received signal considering interference and noise.

**Unit**: dB

**Quality Levels**:
- **Excellent**: > -10 dB
- **Good**: -10 to -15 dB
- **Fair**: -15 to -20 dB
- **Poor**: < -20 dB

**Use Case**:
- More accurate than RSRP in high-interference scenarios
- Better for handover decisions in dense networks

---

### SINR (Signal to Interference plus Noise Ratio)
**Definition**: Ratio of signal power to interference and noise power.

**Unit**: dB

**Quality Levels (LTE/5G)**:
- **Excellent**: > 20 dB
- **Good**: 10-20 dB
- **Fair**: 0-10 dB
- **Poor**: < 0 dB

**Impact on Throughput**:
- High SINR → High throughput
- Low SINR → Reduced throughput, possible connection issues

---

## Technology-Specific KPIs

### 5G NR Specific

#### SSB-RSRP (Synchronization Signal Block RSRP)
- Similar to LTE RSRP but for 5G SSB signals
- Threshold: > -100 dBm

#### gNodeB Utilization
- PRB (Physical Resource Block) usage
- Target: < 80% average, < 95% peak

---

### 4G LTE Specific

#### ERAB Success Rate
- Evolved Radio Access Bearer establishment
- Target: > 98%

#### Inter-eNB Handover Success Rate
- Between different eNodeBs
- Target: > 97%

---

### 3G UMTS Specific

#### RSCP (Received Signal Code Power)
- Similar to RSRP for 3G
- Good: > -95 dBm
- Fair: -95 to -105 dBm
- Poor: < -105 dBm

#### Ec/No (Chip Energy to Noise)
- Signal quality indicator
- Good: > -10 dB
- Fair: -10 to -15 dB
- Poor: < -15 dB

---

## Audit Thresholds

### Critical (Requires Immediate Action)
- Availability < 99.0%
- DCR > 5.0%
- HOSR < 90.0%
- CSSR < 95.0%

### Major (Action Required Within 24h)
- Availability < 99.5%
- DCR > 2.0%
- HOSR < 95.0%
- CSSR < 98.0%

### Minor (Action Required Within Week)
- Availability < 99.8%
- DCR > 1.0%
- HOSR < 97.0%
- CSSR < 98.5%

---

## Best Practices

### KPI Monitoring
1. **Continuous Monitoring**: Track KPIs 24/7 using OSS tools
2. **Trend Analysis**: Compare daily, weekly, monthly trends
3. **Threshold Alerts**: Set up automated alerts for threshold violations
4. **Benchmarking**: Compare against network baseline and industry standards

### Optimization Process
1. **Identify Issues**: Use KPIs to detect problems
2. **Root Cause Analysis**: Investigate underlying causes
3. **Plan Actions**: Develop optimization strategy
4. **Implement Changes**: Execute parameter changes or physical work
5. **Validate Results**: Verify KPI improvement post-change

### Reporting
1. **Daily Reports**: Critical KPIs and major incidents
2. **Weekly Reports**: Trend analysis and optimization progress
3. **Monthly Reports**: Strategic overview and SLA compliance
4. **Executive Reports**: High-level summaries with recommendations

---

## Formulas Reference

### Call Drop Rate
```
DCR = (Number of Dropped Calls / Total Established Calls) × 100
```

### Call Setup Success Rate
```
CSSR = (Successful Call Setups / Total Call Attempts) × 100
```

### Handover Success Rate
```
HOSR = (Successful Handovers / Total Handover Attempts) × 100
```

### Availability
```
Availability = ((Total Time - Unavailable Time) / Total Time) × 100
```

### Average Throughput
```
Average Throughput = Total Data Volume / Total Time
```

---

## Tools Integration

### NetAct (Nokia)
- KPI extraction: NetAct Performance Management
- Real-time monitoring: NetAct Optimizer
- Historical data: NetAct Reporter

### QGIS Integration
- Import KPI data as attributes
- Visualize KPI performance geographically
- Identify spatial patterns and clusters

### Power BI
- Create KPI dashboards
- Automated reporting
- Interactive visualization

---

## References

- 3GPP TS 36.314: E-UTRA Layer 2 - Measurements
- 3GPP TS 38.314: NR Layer 2 - Measurements  
- Nokia NetAct Documentation
- GSMA KPI Guidelines
- Industry SLA Standards

---

**Document Version**: 1.0  
**Last Updated**: October 2025  
**Author**: Helton Lima da Trindade
