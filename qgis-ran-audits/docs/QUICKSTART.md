# Quick Start Guide - QGIS RAN Audits

Welcome to the QGIS RAN Audits project! This guide will help you get started quickly.

## 5-Minute Quick Start

### Step 1: Open the Project
1. Install QGIS from [qgis.org](https://qgis.org/download/) (version 3.x)
2. Download or clone this repository
3. Open QGIS
4. Go to **Project** → **Open**
5. Navigate to `qgis-ran-audits/RAN_Audits.qgs`
6. Click **Open**

### Step 2: Explore the Layers
The project includes four main layers:
- 🔴 **Cell Sites** - Network site locations
- 🔵 **Sectors** - Individual cell sectors
- 🟢 **Coverage Areas** - Signal coverage zones
- 🟡 **Neighbour Relations** - Handover connections

### Step 3: Run Your First Audit
```bash
cd qgis-ran-audits
python3 scripts/ran_audits.py
```

The script will:
- ✅ Check all sites against KPI thresholds
- ✅ Validate neighbour relations
- ✅ Analyze coverage quality
- ✅ Generate a report in `docs/audit_report.json`

### Step 4: Review Results
Open the generated report:
```bash
cat docs/audit_report.json
```

## What's Included

### Sample Data
The project includes sample data for 5 cell sites in Lisbon, Portugal:
- **LIS001**: Lisbon Centro - 5G site
- **LIS002**: Lisbon Parque - 4G/5G site
- **LIS003**: Lisbon Belem - 4G site
- **LIS004**: Lisbon Alfama - 3G/4G site
- **LIS005**: Lisbon Aeroporto - 5G site with 6 sectors

### Audit Features
- ✅ KPI threshold checking (Availability, CSSR, DCR)
- ✅ Neighbour relation validation
- ✅ Coverage analysis
- ✅ Automated issue detection
- ✅ JSON report generation

## Common Tasks

### Add a New Site
1. In QGIS, select the **Cell Sites** layer
2. Click the **Toggle Editing** button (pencil icon)
3. Click **Add Point Feature** button
4. Click on the map where the site is located
5. Fill in the site attributes in the form
6. Click **OK**
7. Click **Save Edits** button

### Customize KPI Thresholds
Edit `config/audit_rules.json`:
```json
{
  "kpi_thresholds": {
    "availability": 99.5,  // Change this value
    "cssr": 98.0,         // Change this value
    "dcr": 2.0            // Change this value
  }
}
```

### Export Data to CSV
1. Right-click on any layer (e.g., Cell Sites)
2. Select **Export** → **Save Features As**
3. Choose format: **Comma Separated Value [CSV]**
4. Select save location
5. Click **OK**

### Create a Map Layout
1. Go to **Project** → **New Print Layout**
2. Add a map: **Add Item** → **Add Map**
3. Draw rectangle on canvas
4. Add title, legend, and scale bar
5. Export: **Layout** → **Export as PDF**

## Understanding the Data

### Cell Sites Attributes
- `site_id`: Unique identifier (e.g., LIS001)
- `technology`: 2G/3G/4G/5G
- `vendor`: Nokia, Ericsson, etc.
- `kpi_availability`: Uptime percentage
- `kpi_cssr`: Call setup success rate
- `kpi_dcr`: Drop call rate
- `audit_status`: Pass/Warning/Fail

### Sectors Attributes
- `sector_id`: Unique identifier (e.g., LIS001_1)
- `azimuth`: Antenna direction (0-360°)
- `beamwidth`: Coverage angle
- `pci`: Physical Cell ID (LTE/5G)
- `hosr`: Handover success rate
- `neighbour_count`: Number of neighbors

## Next Steps

### For Network Planning
1. Import your own site data (GeoJSON, Shapefile, CSV with coordinates)
2. Update KPI values from NetAct or other OSS
3. Run audits before and after optimization
4. Track improvement over time

### For Performance Optimization
1. Focus on sites with `audit_status: Warning` or `Fail`
2. Check sectors with low HOSR
3. Identify missing neighbour relations
4. Analyze coverage gaps

### For Reporting
1. Run weekly audits with the Python script
2. Compare results over time
3. Generate executive summaries
4. Create maps for customer presentations

## Tips & Tricks

### Filtering Data
To show only sites with issues:
1. Right-click **Cell Sites** layer
2. Select **Filter**
3. Enter: `"audit_status" != 'Pass'`
4. Click **OK**

### Styling by KPI
To color-code sites by availability:
1. Right-click **Cell Sites** layer
2. Select **Properties** → **Symbology**
3. Change from **Single Symbol** to **Graduated**
4. Select field: `kpi_availability`
5. Choose color ramp (red to green)
6. Click **Classify** → **OK**

### Measuring Distance
To measure distance between sites:
1. Click **Measure Line** tool (ruler icon)
2. Click on first site
3. Click on second site
4. Double-click to finish
5. Distance is shown in meters

## Troubleshooting

### "Layer not found" error
- Check that all files in `data/` folder exist
- Verify file paths in QGIS project file
- Try opening layers manually: **Layer** → **Add Layer** → **Add Vector Layer**

### Python script doesn't run
- Verify Python 3 is installed: `python3 --version`
- Check you're in the correct directory: `cd qgis-ran-audits`
- Verify data files exist in `data/` subdirectories

### No data visible on map
- Check layer visibility (checkboxes in Layers panel)
- Zoom to layer: Right-click layer → **Zoom to Layer**
- Verify CRS is correct: Bottom-right should show "EPSG:4326"

## Getting Help

### Documentation
- Full documentation: See `README.md`
- Configuration guide: Check `config/audit_rules.json`
- Report template: Review `templates/audit_report_template.md`

### Support
- 📧 Email: heltonlimatrindade@gmail.com
- 🔗 LinkedIn: [heltonlimatrindade](https://www.linkedin.com/in/heltonlimatrindade)
- 💻 GitHub: [heltonlimatrindade](https://github.com/heltonlimatrindade)

## Resources

### QGIS Learning
- [QGIS Documentation](https://docs.qgis.org/)
- [QGIS Training Manual](https://docs.qgis.org/latest/en/docs/training_manual/)
- [QGIS Tutorials](https://www.qgistutorials.com/)

### RAN Engineering
- Nokia NetAct documentation
- 3GPP specifications (TS 36.xxx for LTE, TS 38.xxx for 5G)
- Industry KPI benchmarks

---

**Ready to start?** Open the QGIS project and explore! 🚀

*Last updated: October 2025*
