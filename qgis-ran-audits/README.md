# QGIS RAN Audits Project

A comprehensive QGIS-based project for Radio Access Network (RAN) auditing, analysis, and optimization. This project provides tools and workflows for network engineers to perform systematic audits of 2G/3G/4G/5G networks.

## Overview

This project enables RAN engineers to:
- Visualize cell sites, sectors, and coverage areas on interactive maps
- Perform automated KPI audits against configurable thresholds
- Analyze neighbour relations and handover performance
- Identify network issues and optimization opportunities
- Generate audit reports and documentation

## Project Structure

```
qgis-ran-audits/
├── RAN_Audits.qgs              # Main QGIS project file
├── data/                        # GeoJSON data layers
│   ├── cell_sites/             # Cell site locations and attributes
│   ├── sectors/                # Sector configurations and KPIs
│   ├── coverage/               # Coverage prediction/measurement data
│   └── neighbours/             # Neighbour relation topology
├── scripts/                     # Python automation scripts
│   └── ran_audits.py           # Main audit script
├── config/                      # Configuration files
│   └── audit_rules.json        # KPI thresholds and audit rules
├── templates/                   # Report templates
└── docs/                        # Documentation and reports
```

## Features

### 1. Cell Site Management
- **Site Inventory**: Track all BTS/eNodeB/gNodeB sites with complete metadata
- **Technology Tracking**: Monitor 2G, 3G, 4G, and 5G deployments
- **Vendor Information**: Support for multi-vendor networks (Nokia, Ericsson, Huawei)
- **KPI Monitoring**: Availability, CSSR, DCR, and other critical metrics

### 2. Sector Analysis
- **Configuration Audit**: Azimuth, tilt, power, and antenna parameters
- **PCI Planning**: Physical Cell ID management and conflict detection
- **Coverage Patterns**: Directional coverage visualization
- **Performance Metrics**: HOSR, RRC success rates, throughput

### 3. Neighbour Relations
- **Topology Mapping**: Visual representation of neighbour connections
- **Intra-RAT & Inter-RAT**: Support for same-technology and cross-technology handovers
- **Performance Analysis**: Handover success rate monitoring
- **Missing Neighbours**: Identification of coverage gaps

### 4. Coverage Analysis
- **RSRP/RSRQ Mapping**: Signal strength and quality visualization
- **Coverage Holes**: Identification of weak signal areas
- **Overlap Analysis**: Detection of over-coverage scenarios
- **Population Coverage**: Service area and user impact assessment

## Getting Started

### Prerequisites

- **QGIS 3.x**: Download from [qgis.org](https://qgis.org)
- **Python 3.x**: Required for automation scripts
- **Basic GIS Knowledge**: Understanding of coordinate systems and spatial data

### Installation

1. Clone or download this repository
2. Open QGIS and load the project file: `RAN_Audits.qgs`
3. Verify that all data layers are loaded correctly
4. Install Python dependencies (if needed):
   ```bash
   pip install -r requirements.txt  # If provided
   ```

### Opening the Project

1. Launch QGIS
2. Go to **Project** → **Open**
3. Navigate to the project directory
4. Select `RAN_Audits.qgs`
5. All layers should load automatically with proper styling

## Data Layers

### Cell Sites Layer
Contains point features for each cell site with attributes:
- `site_id`: Unique site identifier
- `site_name`: Human-readable site name
- `vendor`: Equipment vendor (Nokia, Ericsson, Huawei)
- `technology`: Deployed technologies (2G/3G/4G/5G)
- `commission_date`: Site activation date
- `kpi_availability`, `kpi_cssr`, `kpi_dcr`: Key performance indicators
- `audit_status`: Pass/Warning/Fail

### Sectors Layer
Point features representing individual cell sectors:
- `sector_id`: Unique sector identifier
- `azimuth`: Antenna direction (0-360°)
- `beamwidth`: Horizontal antenna beamwidth
- `tilt`: Antenna downtilt angle
- `technology`, `band`, `power`: RF parameters
- `pci`, `tac`: LTE/5G identifiers
- `hosr`, `rrc_success`: Performance metrics

### Coverage Layer
Polygon features showing predicted or measured coverage:
- `coverage_id`: Coverage area identifier
- `rsrp_level`: Signal strength category
- `rsrp_min`, `rsrp_max`: Signal strength range (dBm)
- `area_km2`: Coverage area size
- `population`: Estimated population served

### Neighbour Relations Layer
Line features connecting sectors with neighbour relationships:
- `relation_id`: Unique relation identifier
- `source_sector`, `target_sector`: Connected sectors
- `relation_type`: Intra-RAT or Inter-RAT
- `handover_attempts`, `handover_success`: Performance data
- `hosr`: Handover success rate (%)

## Audit Scripts

### Running the Main Audit Script

The automated audit script checks network data against configurable thresholds:

```bash
cd scripts
python ran_audits.py
```

### Audit Categories

The script performs the following audits:

1. **Site KPI Audit**
   - Checks availability, CSSR, DCR against thresholds
   - Identifies underperforming sites
   - Generates issue list with severity levels

2. **Neighbour Relation Audit**
   - Validates neighbour counts per sector
   - Checks handover success rates
   - Identifies missing or poorly performing relations

3. **Coverage Audit**
   - Analyzes signal strength levels
   - Identifies weak coverage areas
   - Validates coverage quality

### Configuration

Edit `config/audit_rules.json` to customize audit thresholds:

```json
{
  "kpi_thresholds": {
    "availability": 99.5,
    "cssr": 98.0,
    "dcr": 2.0,
    "hosr": 98.0
  },
  "neighbour_rules": {
    "min_neighbours": 6,
    "max_neighbours": 32
  }
}
```

## Use Cases

### 1. Pre-Integration Planning
- Review site locations and coverage predictions
- Validate neighbour lists before site activation
- Check for PCI conflicts and parameter consistency

### 2. Post-Integration Verification
- Verify site activation and initial KPIs
- Confirm neighbour relations are established
- Validate handover performance

### 3. Network Optimization
- Identify underperforming cells and sectors
- Analyze handover failures and dropped calls
- Optimize neighbour lists and RF parameters

### 4. Periodic Audits
- Regular network health checks
- Trend analysis over time
- Compliance verification against SLAs

### 5. Troubleshooting
- Investigate customer complaints
- Analyze coverage gaps
- Root cause analysis for performance issues

## Typical Workflows

### Workflow 1: New Site Audit
1. Add new site to `cell_sites` layer
2. Configure sectors with azimuth and parameters
3. Define predicted coverage areas
4. Configure neighbour relations
5. Run pre-integration audit script
6. Export validation report

### Workflow 2: Performance Optimization
1. Load current KPI data into layers
2. Run audit script to identify issues
3. Visualize problem areas on map
4. Analyze neighbour relations for poor HOSR
5. Plan optimization actions
6. Document changes and expected improvements

### Workflow 3: Coverage Gap Analysis
1. Import drive test or measurement data
2. Overlay with predicted coverage
3. Identify discrepancies
4. Plan infill sites or sector adjustments
5. Generate coverage improvement proposal

## KPI Definitions

| KPI | Description | Target |
|-----|-------------|--------|
| **Availability** | Percentage of time service is available | > 99.5% |
| **CSSR** | Call Setup Success Rate | > 98% |
| **DCR** | Drop Call Rate | < 2% |
| **HOSR** | Handover Success Rate | > 98% |
| **RRC Success** | RRC Connection Success Rate | > 98.5% |
| **RSRP** | Reference Signal Received Power | > -100 dBm |
| **RSRQ** | Reference Signal Received Quality | > -15 dB |

## Customization

### Adding New Sites
1. In QGIS, select the Cell Sites layer
2. Enable editing (toggle edit mode)
3. Add new point feature at site location
4. Fill in all required attributes
5. Save edits

### Modifying Audit Rules
Edit `config/audit_rules.json` to adjust:
- KPI thresholds
- Neighbour count limits
- Technology-specific parameters
- Severity classifications

### Creating Custom Scripts
The `scripts/` directory can contain additional Python scripts:
- Custom KPI calculations
- Import/export utilities
- Integration with NetAct or other tools
- Automated report generation

## Integration Possibilities

### NetAct Integration
- Export site data from NetAct
- Import into QGIS layers
- Visualize Nokia network on maps
- Export optimization scripts back to NetAct

### Power BI Integration
- Export audit results as CSV/JSON
- Import into Power BI for dashboards
- Create executive summaries
- Track KPI trends over time

### Excel/VBA Integration
- Export data for Excel analysis
- Use VBA scripts for batch processing
- Generate customer reports
- MOP (Method of Procedure) creation

## Best Practices

1. **Data Quality**: Keep site data up-to-date with commissioning activities
2. **Regular Audits**: Run automated audits weekly or after major changes
3. **Documentation**: Document all optimization actions and results
4. **Backup**: Maintain regular backups of project and data files
5. **Version Control**: Use Git or similar for project tracking
6. **Validation**: Cross-check QGIS data with live network data
7. **Collaboration**: Share project with team for collaborative analysis

## Technology Reference

### Supported Technologies
- **2G GSM**: 900/1800 MHz
- **3G UMTS**: 900/2100 MHz
- **4G LTE**: B3, B7, B20, B28, B1, B8
- **5G NR**: n78, n28, n1, n3, n7

### Vendor Support
- **Nokia**: Full support for NetAct export/import
- **Ericsson**: OSS-RC data integration
- **Huawei**: eNodeB Manager export compatibility

### Frequency Bands
- **LTE Band 3**: 1800 MHz (1710-1785 / 1805-1880)
- **LTE Band 7**: 2600 MHz (2500-2570 / 2620-2690)
- **LTE Band 20**: 800 MHz (832-862 / 791-821)
- **5G n78**: 3500 MHz (3300-3800)

## Troubleshooting

### Layer Not Loading
- Check file paths in project file
- Verify GeoJSON files are valid
- Ensure CRS (Coordinate Reference System) is correct

### Script Errors
- Verify Python version (3.x required)
- Check file paths in scripts
- Ensure all data files exist

### Missing Data
- Populate data layers with actual network data
- Use sample data for testing
- Import from NetAct or other OSS

## Contributing

Improvements and additions are welcome:
- Additional audit scripts
- New data visualization styles
- Enhanced reporting templates
- Integration with other tools

## License

This project is provided as-is for RAN engineering purposes.

## Contact

**Helton Lima da Trindade**  
Senior RAN Engineer  
📧 heltonlimatrindade@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/heltonlimatrindade)  
💻 [GitHub](https://github.com/heltonlimatrindade)

---

**Version**: 1.0  
**Last Updated**: October 2025  
**QGIS Version**: 3.28+  
**Status**: Production Ready
