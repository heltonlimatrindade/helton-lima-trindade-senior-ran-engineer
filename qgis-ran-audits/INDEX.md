# QGIS RAN Audits - Project Index

Welcome to the QGIS RAN Audits project! This document serves as a comprehensive index to help you navigate all project resources.

## 📁 Project Structure

```
qgis-ran-audits/
├── RAN_Audits.qgs              # Main QGIS project file - START HERE
├── README.md                    # Complete project documentation
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
│
├── data/                        # GeoJSON data layers
│   ├── cell_sites/
│   │   └── cell_sites.geojson  # 5 sample cell sites (Lisbon area)
│   ├── sectors/
│   │   └── sectors.geojson     # 6 sample sectors with KPIs
│   ├── coverage/
│   │   └── coverage.geojson    # 3 coverage prediction areas
│   └── neighbours/
│       └── neighbours.geojson  # 5 neighbour relations
│
├── scripts/                     # Python automation scripts
│   └── ran_audits.py           # Main audit automation script
│
├── config/                      # Configuration files
│   └── audit_rules.json        # KPI thresholds and audit rules
│
├── templates/                   # Report templates
│   └── audit_report_template.md # Markdown report template
│
└── docs/                        # Documentation
    ├── QUICKSTART.md            # 5-minute quick start guide
    ├── KPI_REFERENCE.md         # Complete KPI definitions
    ├── ARCHITECTURE.md          # System architecture & data flow
    └── audit_report.json        # Sample generated audit report
```

## 🚀 Getting Started

### For First-Time Users
1. **[Quick Start Guide](docs/QUICKSTART.md)** - Get up and running in 5 minutes
2. **[Main README](README.md)** - Complete documentation and features
3. **[Open QGIS Project](RAN_Audits.qgs)** - Launch the visualization

### For RAN Engineers
1. Review **[KPI Reference](docs/KPI_REFERENCE.md)** for threshold definitions
2. Understand **[Architecture](docs/ARCHITECTURE.md)** for data flow
3. Run the audit script: `python3 scripts/ran_audits.py`
4. Customize **[Audit Rules](config/audit_rules.json)** for your network

## 📚 Documentation Index

### Core Documentation
| Document | Purpose | Target Audience |
|----------|---------|----------------|
| [README.md](README.md) | Complete project guide | All users |
| [QUICKSTART.md](docs/QUICKSTART.md) | Fast setup & basic usage | New users |
| [KPI_REFERENCE.md](docs/KPI_REFERENCE.md) | KPI definitions & formulas | Engineers, Analysts |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | System design & data flow | Technical users, Developers |

### Templates & Configuration
| File | Purpose | Usage |
|------|---------|-------|
| [audit_rules.json](config/audit_rules.json) | KPI thresholds configuration | Edit to customize audits |
| [audit_report_template.md](templates/audit_report_template.md) | Report structure template | Reference for custom reports |

### Sample Data
| Layer | File | Description |
|-------|------|-------------|
| Cell Sites | [cell_sites.geojson](data/cell_sites/cell_sites.geojson) | 5 sites (2G/3G/4G/5G) |
| Sectors | [sectors.geojson](data/sectors/sectors.geojson) | 6 sectors with RF parameters |
| Coverage | [coverage.geojson](data/coverage/coverage.geojson) | 3 coverage prediction areas |
| Neighbours | [neighbours.geojson](data/neighbours/neighbours.geojson) | 5 handover relations |

## 🔧 Key Components

### 1. QGIS Project File
**File**: `RAN_Audits.qgs`  
**Purpose**: Main visualization and analysis interface  
**Contents**:
- Pre-configured layers for all RAN data
- WGS 84 coordinate system (EPSG:4326)
- Proper layer styling and symbology
- Map extent centered on Lisbon, Portugal

### 2. Audit Script
**File**: `scripts/ran_audits.py`  
**Purpose**: Automated network auditing  
**Features**:
- Site KPI validation
- Neighbour relation audits
- Coverage quality analysis
- JSON report generation

**Usage**:
```bash
cd qgis-ran-audits
python3 scripts/ran_audits.py
```

### 3. Configuration
**File**: `config/audit_rules.json`  
**Purpose**: Configurable audit thresholds  
**Key Sections**:
- `kpi_thresholds`: Availability, CSSR, DCR, HOSR
- `neighbour_rules`: Min/max neighbour counts
- `coverage_rules`: RSRP signal strength thresholds
- `technology_specific`: 5G, 4G, 3G parameters

### 4. Sample Data
**Location**: `data/` directory  
**Format**: GeoJSON (RFC 7946)  
**Coverage**: Lisbon metropolitan area (Portugal)  
**Purpose**: 
- Demonstration of project capabilities
- Testing and validation
- Template for real network data

## 📊 Workflows

### Common Use Cases

#### 1. Pre-Integration Planning
```
1. Import site plan → data/cell_sites/
2. Configure sectors → data/sectors/
3. Define neighbours → data/neighbours/
4. Run audit script
5. Review validation report
```

#### 2. Network Optimization
```
1. Export current KPIs from NetAct
2. Import into QGIS layers
3. Visualize problem areas on map
4. Run audit to identify issues
5. Plan optimization actions
6. Document expected improvements
```

#### 3. Regular Health Checks
```
1. Weekly: Run audit script
2. Review generated report
3. Track issues over time
4. Update documentation
5. Present to stakeholders
```

## 🛠️ Technical Details

### Data Format: GeoJSON
- **Standard**: RFC 7946
- **Coordinate System**: WGS 84 (EPSG:4326)
- **Geometry Types**: Point, LineString, Polygon
- **Why GeoJSON**: Human-readable, web-compatible, QGIS-native

### Technology Support
- **2G GSM**: 900/1800 MHz
- **3G UMTS**: 900/2100 MHz
- **4G LTE**: Bands 3, 7, 20, 28
- **5G NR**: n78, n28 (NSA & SA)

### Vendor Compatibility
- **Nokia**: NetAct exports, full compatibility
- **Ericsson**: OSS-RC data support
- **Huawei**: eNodeB Manager integration
- **Multi-vendor**: Normalized data model

## 📈 KPI Summary

| KPI | Target | Critical | Purpose |
|-----|--------|----------|---------|
| Availability | ≥ 99.5% | < 99.0% | Service uptime |
| CSSR | ≥ 98.0% | < 95.0% | Call setup success |
| DCR | ≤ 2.0% | > 5.0% | Call drop rate |
| HOSR | ≥ 98.0% | < 90.0% | Handover success |

See [KPI_REFERENCE.md](docs/KPI_REFERENCE.md) for complete definitions.

## 🎯 Project Features

### Visualization
✅ Interactive maps with multiple layers  
✅ Color-coded KPI indicators  
✅ Directional sector representation  
✅ Coverage area overlays  
✅ Neighbour topology lines  

### Analysis
✅ Automated KPI threshold checking  
✅ Neighbour relation validation  
✅ Coverage quality assessment  
✅ Issue prioritization (Critical/Major/Minor)  

### Reporting
✅ JSON audit reports  
✅ Issue summaries and statistics  
✅ Export to CSV/Excel  
✅ Map layout generation  
✅ Custom report templates  

### Automation
✅ Python scripting support  
✅ Batch processing capability  
✅ Scheduled audit execution  
✅ Integration with external tools  

## 🔗 Integration Points

### Input Sources
- Nokia NetAct (CSV/XML export)
- Ericsson OSS-RC (XML export)
- Huawei U2000 (JSON export)
- Drive test tools (MapInfo, CSV)
- Coverage prediction tools

### Output Targets
- Power BI dashboards
- Excel/VBA analysis
- SharePoint documentation
- PDF reports for customers
- Web-based dashboards

## 🎓 Learning Resources

### QGIS
- [QGIS Official Documentation](https://docs.qgis.org/)
- [QGIS Training Manual](https://docs.qgis.org/latest/en/docs/training_manual/)
- [QGIS Tutorials](https://www.qgistutorials.com/)

### RAN Engineering
- 3GPP Specifications (TS 36.xxx for LTE, TS 38.xxx for 5G)
- Nokia NetAct User Guides
- GSMA KPI Guidelines

### Python & GIS
- [Python GIS Programming](https://automating-gis-processes.github.io/)
- [PyQGIS Cookbook](https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/)

## 📞 Support & Contact

**Project Maintainer**: Helton Lima da Trindade  
**Role**: Senior RAN Engineer  
**Company**: Nokia Networks

**Contact**:
- 📧 Email: heltonlimatrindade@gmail.com
- 🔗 LinkedIn: [heltonlimatrindade](https://www.linkedin.com/in/heltonlimatrindade)
- 💻 GitHub: [heltonlimatrindade](https://github.com/heltonlimatrindade)
- 💬 WhatsApp: +351 962 462 317

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Oct 2025 | Initial release with complete structure |

## 🔄 Next Steps

### To Get Started
1. ✅ Read [QUICKSTART.md](docs/QUICKSTART.md)
2. ✅ Open QGIS project
3. ✅ Run sample audit script
4. ✅ Review generated report

### To Customize
1. Edit `config/audit_rules.json` with your thresholds
2. Replace sample data with your network data
3. Customize layer styling in QGIS
4. Modify scripts for your workflows

### To Extend
1. Add new audit scripts in `scripts/`
2. Create custom data layers
3. Develop integration with your OSS
4. Build automated reporting pipelines

## 📄 License

This project is provided as-is for RAN engineering and network optimization purposes.

---

**Last Updated**: October 2025  
**QGIS Version**: 3.28+  
**Python Version**: 3.x  
**Status**: Production Ready ✅

For the most up-to-date information, see the [main README](README.md).
