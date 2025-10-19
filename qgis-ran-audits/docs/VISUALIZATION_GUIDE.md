# Data Visualization Guide

## Overview

This guide explains how data is visualized in the QGIS RAN Audits project and provides styling recommendations.

## Layer Styling

### Cell Sites Layer

**Geometry**: Point  
**Recommended Symbol**: Circle with site icon overlay

**Style by Audit Status**:
```
Pass    → Green circle (●) RGB(46, 204, 113)
Warning → Orange circle (●) RGB(243, 156, 18)
Fail    → Red circle (●) RGB(231, 76, 60)
```

**Symbol Size**: 8-12 pixels  
**Label Field**: `site_name`  
**Label Size**: 10pt, bold

**Advanced Styling**:
- Use graduated symbols for KPI values
- Color ramp: Red (bad) → Yellow (fair) → Green (good)
- Graduated by: `kpi_availability` or `kpi_cssr`

### Sectors Layer

**Geometry**: Point  
**Recommended Symbol**: Directional arrow or pie slice

**Style by Technology**:
```
5G  → Purple (●) RGB(155, 89, 182)
4G  → Blue (●) RGB(52, 152, 219)
3G  → Green (●) RGB(46, 204, 113)
2G  → Gray (●) RGB(149, 165, 166)
```

**Rotation Field**: `azimuth` (0-360 degrees)  
**Symbol**: Arrow or triangle pointing upward (0° = North)  
**Size**: 6-10 pixels

**Label Content**: `sector_id` + `pci`  
Example: "LIS001_1 (PCI:100)"

### Coverage Areas Layer

**Geometry**: Polygon  
**Recommended Style**: Semi-transparent fill

**Style by RSRP Level**:
```
Excellent → Dark Green, 30% opacity
Good      → Light Green, 30% opacity
Fair      → Yellow, 30% opacity
Poor      → Red, 30% opacity
```

**Border**: 1 pixel, darker shade of fill color  
**Label Field**: `coverage_id`  
**Label Position**: Center of polygon

**RSRP Color Scale**:
- < -110 dBm: Red (Very Poor)
- -110 to -100 dBm: Orange (Poor)
- -100 to -90 dBm: Yellow (Fair)
- -90 to -80 dBm: Light Green (Good)
- > -80 dBm: Dark Green (Excellent)

### Neighbour Relations Layer

**Geometry**: LineString  
**Recommended Style**: Arrows showing direction

**Style by HOSR**:
```
> 98%    → Green line, 2px
95-98%   → Yellow line, 2px
90-95%   → Orange line, 2px
< 90%    → Red line, 3px (bold)
```

**Line Style**: 
- Solid for active relations
- Dashed for proposed/planned relations
- Arrow at target end

**Label Field**: `hosr` (handover success rate %)

## Map Composition

### Recommended Layer Order (top to bottom)
1. Labels (always on top)
2. Neighbour Relations (lines)
3. Sectors (points with direction)
4. Cell Sites (points)
5. Coverage Areas (polygons)
6. Base Map (OpenStreetMap, Google, etc.)

### Base Map Options

**OpenStreetMap (Free)**:
- URL: `https://tile.openstreetmap.org/{z}/{x}/{y}.png`
- Type: XYZ Tiles
- Best for: General reference

**Google Satellite (if available)**:
- Best for: Rural areas, site location verification

**CartoDB Light (Free)**:
- URL: `https://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png`
- Best for: Clean, professional presentations

## Visual Examples

### Cell Site Representation
```
      ●  LIS001 (5G)
     ↗ ↑ ↖          Sectors showing azimuth
      \|/           Three-sector configuration
       ●            Site location
```

### Coverage Visualization
```
   ┌─────────────┐
   │ Excellent   │  -80 dBm  (Dark Green)
   ├─────────────┤
   │ Good        │  -95 dBm  (Light Green)
   ├─────────────┤
   │ Fair        │  -105 dBm (Yellow)
   ├─────────────┤
   │ Poor        │  -110 dBm (Orange/Red)
   └─────────────┘
```

### Neighbour Relations
```
Site A ────────► Site B  (Green: Good HOSR)
Site C --------- Site D  (Dashed: Planned)
Site E ▬▬▬▬▬▬▬► Site F  (Red Bold: Poor HOSR)
```

## Color Schemes

### Standard Network Colors
```css
/* Good / Pass */
Green:  #2ecc71  RGB(46, 204, 113)

/* Warning / Attention */
Yellow: #f39c12  RGB(243, 156, 18)
Orange: #e67e22  RGB(230, 126, 34)

/* Critical / Fail */
Red:    #e74c3c  RGB(231, 76, 60)

/* Neutral / Inactive */
Gray:   #95a5a6  RGB(149, 165, 166)
```

### Technology Colors
```css
/* 5G */
Purple: #9b59b6  RGB(155, 89, 182)

/* 4G/LTE */
Blue:   #3498db  RGB(52, 152, 219)

/* 3G/UMTS */
Green:  #2ecc71  RGB(46, 204, 113)

/* 2G/GSM */
Gray:   #7f8c8d  RGB(127, 140, 141)
```

## Label Styling

### Site Labels
```
Font: Arial Bold 10pt
Color: Black with white halo (2px)
Placement: Above point
Format: {site_id} - {technology}
Example: "LIS001 - 5G"
```

### Sector Labels
```
Font: Arial 8pt
Color: Dark Gray
Placement: Right of point
Format: {sector_id} ({pci})
Example: "LIS001_1 (100)"
```

### Coverage Labels
```
Font: Arial 9pt
Color: Black
Placement: Center
Format: {coverage_type} - {rsrp_level}
Example: "Predicted - Good"
```

## Map Layouts for Printing/Export

### Executive Summary Layout
**Size**: A4 Landscape  
**Elements**:
- Title: "RAN Network Overview"
- Map: 80% of page
- Legend: Right side panel
- Scale bar: Bottom left
- North arrow: Top right
- Date and author: Bottom right

### Detailed Technical Layout
**Size**: A3 Landscape  
**Elements**:
- Main map: 70% of page
- KPI table: Below map
- Site details: Right panel
- Multiple scale bars for different areas
- Grid overlay for coordinates

### Focus Area Layout
**Size**: A4 Portrait  
**Elements**:
- Zoomed to specific area
- Detailed labels for all features
- Site photos (if available)
- Technical parameters table
- Notes section

## Interactive Features

### Identify Tool
Click on any feature to see:
- Cell Sites: All site attributes + KPIs
- Sectors: RF parameters + performance
- Coverage: RSRP levels + area size
- Relations: Handover statistics

### Measurement Tools
- Distance between sites
- Area of coverage polygons
- Bearing/azimuth between points

### Filtering
Create filters for:
- Sites with KPI issues
- Sectors with low HOSR
- Coverage below threshold
- Relations needing optimization

## Dynamic Styling with Expressions

### Color Sites by Availability
```python
CASE
  WHEN "kpi_availability" >= 99.5 THEN '#2ecc71'
  WHEN "kpi_availability" >= 99.0 THEN '#f39c12'
  ELSE '#e74c3c'
END
```

### Size Sectors by Neighbour Count
```python
CASE
  WHEN "neighbour_count" < 6 THEN 8
  WHEN "neighbour_count" > 32 THEN 12
  ELSE 10
END
```

### Style Relations by Technology
```python
CASE
  WHEN "relation_type" = 'Inter-RAT' THEN '#9b59b6'
  WHEN "relation_type" = 'Intra-RAT' THEN '#3498db'
  ELSE '#95a5a6'
END
```

## Heat Maps

### KPI Heat Map
Create a heat map showing availability:
1. Use Cell Sites layer
2. Symbology → Heat Map
3. Weight field: `kpi_availability`
4. Color ramp: Red → Yellow → Green
5. Radius: 500-1000 meters

### Coverage Density
Show overlapping coverage areas:
1. Use Coverage layer
2. Count overlapping polygons
3. Color by density
4. Identify over-coverage zones

## Export Settings

### For Presentations
- Format: PNG
- Resolution: 300 DPI
- Size: 1920x1080 (HD)
- Transparent background: No

### For Documentation
- Format: PDF
- Vector graphics: Yes
- Embed fonts: Yes
- Resolution: 300 DPI

### For Web
- Format: PNG or WebP
- Resolution: 150 DPI
- Size: Optimized for screen
- Compression: Medium

## Tips & Tricks

1. **Layer Blending**: Use "Multiply" or "Overlay" blend modes for coverage layers over base maps

2. **Data-Defined Properties**: Use field values to control symbol size, color, and rotation dynamically

3. **Rule-Based Styling**: Create complex styling rules based on multiple conditions

4. **Spatial Bookmarks**: Save frequently viewed areas for quick access

5. **Print Templates**: Create reusable print layouts for consistent reporting

6. **3D Visualization**: Use QGIS 3D views for terrain-aware site placement

## Accessibility

- Use colorblind-friendly palettes
- Include patterns in addition to colors
- Ensure sufficient contrast
- Provide legends for all symbols
- Use clear, readable fonts

---

**Document Version**: 1.0  
**Last Updated**: October 2025  
**For**: QGIS 3.28+
