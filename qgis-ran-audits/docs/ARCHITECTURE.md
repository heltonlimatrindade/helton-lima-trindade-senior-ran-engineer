# QGIS RAN Audits - Project Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    QGIS RAN Audits System                       │
└─────────────────────────────────────────────────────────────────┘
                                │
                ┌───────────────┴───────────────┐
                │                               │
        ┌───────▼────────┐             ┌───────▼────────┐
        │   QGIS UI      │             │  Python Scripts │
        │  Visualization │             │   Automation    │
        └───────┬────────┘             └───────┬────────┘
                │                               │
                └───────────────┬───────────────┘
                                │
                    ┌───────────▼──────────┐
                    │   Data Layer         │
                    │   GeoJSON Files      │
                    └───────────┬──────────┘
                                │
        ┌───────────┬───────────┼───────────┬───────────┐
        │           │           │           │           │
   ┌────▼────┐ ┌───▼────┐ ┌───▼────┐ ┌───▼────┐ ┌───▼────┐
   │  Cell   │ │Sectors │ │Coverage│ │Neighbour│ │ Config │
   │  Sites  │ │        │ │        │ │ Relations│ │ Rules  │
   └─────────┘ └────────┘ └────────┘ └─────────┘ └────────┘
```

## Component Architecture

### 1. Presentation Layer (QGIS)

```
┌─────────────────────────────────────────────────────────────┐
│                        QGIS Desktop                         │
├─────────────────────────────────────────────────────────────┤
│  Map Canvas                                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  ● Cell Sites (Points)                               │  │
│  │  ● Sectors (Points with directional attributes)      │  │
│  │  ● Coverage Areas (Polygons)                         │  │
│  │  ● Neighbour Relations (Lines)                       │  │
│  │  ● Base Maps (OSM, Google, etc.)                     │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  Layers Panel    │  Browser Panel  │  Processing Toolbox   │
│  ├ Cell Sites    │  ├ GeoJSON      │  ├ Vector Tools       │
│  ├ Sectors       │  ├ Shapefiles   │  ├ Analysis          │
│  ├ Coverage      │  ├ CSV          │  └ Scripts           │
│  └ Neighbours    │  └ Database     │                       │
└─────────────────────────────────────────────────────────────┘
```

### 2. Application Layer (Python Scripts)

```
┌───────────────────────────────────────────────────────┐
│              ran_audits.py (Main Script)              │
├───────────────────────────────────────────────────────┤
│                                                       │
│  ┌─────────────────────────────────────────────┐    │
│  │         RANAuditor Class                     │    │
│  ├─────────────────────────────────────────────┤    │
│  │ Methods:                                     │    │
│  │  • load_config()                             │    │
│  │  • load_geojson()                            │    │
│  │  • audit_site_kpis()                         │    │
│  │  • audit_neighbour_relations()               │    │
│  │  • audit_coverage()                          │    │
│  │  • generate_report()                         │    │
│  │  • run_full_audit()                          │    │
│  └─────────────────────────────────────────────┘    │
│                                                       │
│  Dependencies: json, os, datetime, pathlib            │
└───────────────────────────────────────────────────────┘
```

### 3. Data Layer

```
┌─────────────────────────────────────────────────────────────┐
│                      Data Structure                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Cell Sites (cell_sites.geojson)                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Properties:                                          │  │
│  │  - site_id, site_name, vendor                        │  │
│  │  - technology, status, commission_date               │  │
│  │  - kpi_availability, kpi_cssr, kpi_dcr               │  │
│  │  - audit_status                                      │  │
│  │ Geometry: Point (longitude, latitude)                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  Sectors (sectors.geojson)                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Properties:                                          │  │
│  │  - sector_id, azimuth, beamwidth, height, tilt       │  │
│  │  - technology, band, power, pci, tac                 │  │
│  │  - neighbour_count, hosr, rrc_success                │  │
│  │ Geometry: Point (same as parent site)                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  Coverage (coverage.geojson)                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Properties:                                          │  │
│  │  - coverage_id, site_id, technology                  │  │
│  │  - rsrp_level, rsrp_min, rsrp_max                    │  │
│  │  - area_km2, population                              │  │
│  │ Geometry: Polygon (coverage boundary)                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  Neighbours (neighbours.geojson)                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Properties:                                          │  │
│  │  - relation_id, source_sector, target_sector         │  │
│  │  - relation_type, technology                         │  │
│  │  - handover_attempts, handover_success, hosr         │  │
│  │ Geometry: LineString (source to target)              │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 4. Configuration Layer

```
┌──────────────────────────────────────────────────┐
│           audit_rules.json                       │
├──────────────────────────────────────────────────┤
│  {                                               │
│    "kpi_thresholds": {                           │
│      "availability": 99.5,                       │
│      "cssr": 98.0,                               │
│      "dcr": 2.0,                                 │
│      "hosr": 98.0                                │
│    },                                            │
│    "neighbour_rules": {                          │
│      "min_neighbours": 6,                        │
│      "max_neighbours": 32,                       │
│      "hosr_threshold": 95.0                      │
│    },                                            │
│    "coverage_rules": {                           │
│      "min_rsrp": -110,                           │
│      "target_rsrp": -95                          │
│    }                                             │
│  }                                               │
└──────────────────────────────────────────────────┘
```

## Data Flow

### Audit Workflow

```
┌─────────────┐
│   START     │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Load Configuration │
│  (audit_rules.json) │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Load GeoJSON Data  │
│  - Cell Sites       │
│  - Sectors          │
│  - Coverage         │
│  - Neighbours       │
└──────┬──────────────┘
       │
       ├──────────────────────────┬──────────────────────────┐
       ▼                          ▼                          ▼
┌──────────────┐       ┌──────────────────┐      ┌─────────────────┐
│  Site KPI    │       │  Neighbour       │      │  Coverage       │
│  Audit       │       │  Relations Audit │      │  Analysis       │
│              │       │                  │      │                 │
│  Check:      │       │  Check:          │      │  Check:         │
│  - Avail.    │       │  - Count         │      │  - RSRP         │
│  - CSSR      │       │  - HOSR          │      │  - Quality      │
│  - DCR       │       │  - Missing       │      │  - Coverage     │
└──────┬───────┘       └────────┬─────────┘      └────────┬────────┘
       │                        │                         │
       └────────────┬───────────┴────────────┬────────────┘
                    ▼                        │
            ┌───────────────┐               │
            │  Collect      │               │
            │  Issues       │               │
            └───────┬───────┘               │
                    │                        │
                    ▼                        ▼
            ┌────────────────────────────────────┐
            │  Generate Audit Report             │
            │  - JSON format                     │
            │  - Summary statistics              │
            │  - Detailed issues list            │
            └────────┬───────────────────────────┘
                     │
                     ▼
            ┌────────────────┐
            │  Save Report   │
            │  to docs/      │
            └────────┬───────┘
                     │
                     ▼
            ┌─────────────┐
            │    END      │
            └─────────────┘
```

## Integration Points

### Input Sources
```
┌─────────────────────────────────────────────────────┐
│              External Data Sources                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Nokia NetAct  →  CSV Export  →  Import to QGIS    │
│  Ericsson OSS  →  XML Export  →  Transform & Load  │
│  Huawei U2000  →  JSON Export →  GeoJSON Conversion│
│                                                     │
│  Drive Test    →  MapInfo     →  Shapefile Import  │
│  Predictions   →  CSV         →  Join with Sites   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Output Targets
```
┌─────────────────────────────────────────────────────┐
│              Export & Reporting                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  QGIS Maps     →  PDF/PNG     →  Documentation     │
│  Audit Reports →  JSON        →  Dashboard Input   │
│  KPI Data      →  CSV         →  Excel Analysis    │
│  Site Lists    →  CSV/Excel   →  Implementation    │
│                                                     │
│  Power BI      ←  JSON/CSV    ←  Audit Results     │
│  SharePoint    ←  PDF Reports ←  QGIS Layouts      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## Technology Stack

```
┌──────────────────────────────────────────────────┐
│            Technology Components                 │
├──────────────────────────────────────────────────┤
│                                                  │
│  Desktop GIS:    QGIS 3.28+                      │
│  Scripting:      Python 3.x                      │
│  Data Format:    GeoJSON (RFC 7946)              │
│  Coordinate Sys: WGS 84 (EPSG:4326)              │
│  Config Format:  JSON                            │
│  Reports:        JSON, Markdown                  │
│                                                  │
│  Optional:                                       │
│    - pandas (data analysis)                      │
│    - matplotlib (visualization)                  │
│    - openpyxl (Excel export)                     │
│                                                  │
└──────────────────────────────────────────────────┘
```

## Security & Access Control

```
┌──────────────────────────────────────────────────┐
│            Security Considerations               │
├──────────────────────────────────────────────────┤
│                                                  │
│  • Read-only access to production OSS data       │
│  • No direct network element access              │
│  • Local file-based storage (no DB required)     │
│  • Version control with Git                      │
│  • Sensitive data anonymization recommended      │
│  • Export controls for customer data             │
│                                                  │
└──────────────────────────────────────────────────┘
```

## Scalability

```
┌──────────────────────────────────────────────────┐
│         Scalability & Performance                │
├──────────────────────────────────────────────────┤
│                                                  │
│  Current Capacity:                               │
│    • Sites: 10,000+                              │
│    • Sectors: 30,000+                            │
│    • Relations: 100,000+                         │
│                                                  │
│  Performance:                                    │
│    • Audit Script: < 5 seconds for 1K sites      │
│    • QGIS Loading: < 10 seconds for full data    │
│    • Map Rendering: Real-time                    │
│                                                  │
│  Optimization:                                   │
│    • Spatial indexing for large datasets         │
│    • Layer simplification for visualization      │
│    • Cached coverage calculations                │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

**Document Version**: 1.0  
**Last Updated**: October 2025  
**Author**: Helton Lima da Trindade
