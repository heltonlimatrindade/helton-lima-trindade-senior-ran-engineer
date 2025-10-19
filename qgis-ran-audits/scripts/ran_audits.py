#!/usr/bin/env python3
"""
RAN Network Audit Script
Performs automated audits on RAN network data including:
- KPI threshold checks
- Neighbour relation validation
- Coverage analysis
- Site configuration audits
"""

import json
import os
from datetime import datetime
from pathlib import Path


class RANAuditor:
    """Main class for RAN network audits"""
    
    def __init__(self, config_path="config/audit_rules.json"):
        """Initialize the auditor with configuration"""
        self.config_path = config_path
        self.config = self.load_config()
        self.audit_results = []
        
    def load_config(self):
        """Load audit configuration from JSON file"""
        config_file = Path(__file__).parent.parent / self.config_path
        if config_file.exists():
            with open(config_file, 'r') as f:
                return json.load(f)
        return self.default_config()
    
    def default_config(self):
        """Return default audit configuration"""
        return {
            "kpi_thresholds": {
                "availability": 99.5,
                "cssr": 98.0,
                "dcr": 2.0,
                "hosr": 98.0,
                "rrc_success": 98.5
            },
            "neighbour_rules": {
                "min_neighbours": 6,
                "max_neighbours": 32,
                "hosr_threshold": 95.0
            },
            "coverage_rules": {
                "min_rsrp": -110,
                "target_rsrp": -95
            }
        }
    
    def load_geojson(self, filepath):
        """Load GeoJSON data from file"""
        full_path = Path(__file__).parent.parent / filepath
        if full_path.exists():
            with open(full_path, 'r') as f:
                return json.load(f)
        return None
    
    def audit_site_kpis(self, cell_sites_data):
        """Audit cell site KPIs against thresholds"""
        print("\n=== Auditing Site KPIs ===")
        issues = []
        
        thresholds = self.config["kpi_thresholds"]
        
        for feature in cell_sites_data.get("features", []):
            props = feature["properties"]
            site_id = props.get("site_id", "Unknown")
            
            # Check availability
            if props.get("kpi_availability", 100) < thresholds["availability"]:
                issues.append({
                    "site_id": site_id,
                    "issue": "Low Availability",
                    "value": props.get("kpi_availability"),
                    "threshold": thresholds["availability"]
                })
            
            # Check CSSR
            if props.get("kpi_cssr", 100) < thresholds["cssr"]:
                issues.append({
                    "site_id": site_id,
                    "issue": "Low CSSR",
                    "value": props.get("kpi_cssr"),
                    "threshold": thresholds["cssr"]
                })
            
            # Check DCR
            if props.get("kpi_dcr", 0) > thresholds["dcr"]:
                issues.append({
                    "site_id": site_id,
                    "issue": "High DCR",
                    "value": props.get("kpi_dcr"),
                    "threshold": thresholds["dcr"]
                })
        
        self.audit_results.append({
            "audit_type": "Site KPIs",
            "total_sites": len(cell_sites_data.get("features", [])),
            "issues_found": len(issues),
            "issues": issues
        })
        
        print(f"Total sites checked: {len(cell_sites_data.get('features', []))}")
        print(f"Issues found: {len(issues)}")
        for issue in issues:
            print(f"  - {issue['site_id']}: {issue['issue']} (Value: {issue['value']}, Threshold: {issue['threshold']})")
        
        return issues
    
    def audit_neighbour_relations(self, sectors_data, neighbours_data):
        """Audit neighbour relations for completeness and performance"""
        print("\n=== Auditing Neighbour Relations ===")
        issues = []
        
        rules = self.config["neighbour_rules"]
        
        # Check sector neighbour counts
        for feature in sectors_data.get("features", []):
            props = feature["properties"]
            sector_id = props.get("sector_id", "Unknown")
            neighbour_count = props.get("neighbour_count", 0)
            
            if neighbour_count < rules["min_neighbours"]:
                issues.append({
                    "sector_id": sector_id,
                    "issue": "Insufficient neighbours",
                    "neighbour_count": neighbour_count,
                    "minimum": rules["min_neighbours"]
                })
            elif neighbour_count > rules["max_neighbours"]:
                issues.append({
                    "sector_id": sector_id,
                    "issue": "Too many neighbours",
                    "neighbour_count": neighbour_count,
                    "maximum": rules["max_neighbours"]
                })
        
        # Check neighbour relation HOSR
        for feature in neighbours_data.get("features", []):
            props = feature["properties"]
            relation_id = props.get("relation_id", "Unknown")
            hosr = props.get("hosr", 100)
            
            if hosr < rules["hosr_threshold"]:
                issues.append({
                    "relation_id": relation_id,
                    "source": props.get("source_sector"),
                    "target": props.get("target_sector"),
                    "issue": "Low HOSR",
                    "hosr": hosr,
                    "threshold": rules["hosr_threshold"]
                })
        
        self.audit_results.append({
            "audit_type": "Neighbour Relations",
            "total_sectors": len(sectors_data.get("features", [])),
            "total_relations": len(neighbours_data.get("features", [])),
            "issues_found": len(issues),
            "issues": issues
        })
        
        print(f"Total sectors checked: {len(sectors_data.get('features', []))}")
        print(f"Total relations checked: {len(neighbours_data.get('features', []))}")
        print(f"Issues found: {len(issues)}")
        for issue in issues:
            print(f"  - {issue}")
        
        return issues
    
    def audit_coverage(self, coverage_data):
        """Audit coverage areas for signal strength"""
        print("\n=== Auditing Coverage Areas ===")
        issues = []
        
        rules = self.config["coverage_rules"]
        
        for feature in coverage_data.get("features", []):
            props = feature["properties"]
            coverage_id = props.get("coverage_id", "Unknown")
            rsrp_min = props.get("rsrp_min", 0)
            
            if rsrp_min < rules["min_rsrp"]:
                issues.append({
                    "coverage_id": coverage_id,
                    "site_id": props.get("site_id"),
                    "issue": "Weak coverage",
                    "rsrp_min": rsrp_min,
                    "threshold": rules["min_rsrp"]
                })
        
        self.audit_results.append({
            "audit_type": "Coverage Analysis",
            "total_areas": len(coverage_data.get("features", [])),
            "issues_found": len(issues),
            "issues": issues
        })
        
        print(f"Total coverage areas checked: {len(coverage_data.get('features', []))}")
        print(f"Issues found: {len(issues)}")
        for issue in issues:
            print(f"  - {issue}")
        
        return issues
    
    def generate_report(self, output_path="docs/audit_report.json"):
        """Generate audit report in JSON format"""
        report = {
            "report_date": datetime.now().isoformat(),
            "audits": self.audit_results,
            "summary": {
                "total_audits": len(self.audit_results),
                "total_issues": sum(audit["issues_found"] for audit in self.audit_results)
            }
        }
        
        output_file = Path(__file__).parent.parent / output_path
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n=== Audit Report Generated ===")
        print(f"Report saved to: {output_file}")
        print(f"Total audits performed: {report['summary']['total_audits']}")
        print(f"Total issues found: {report['summary']['total_issues']}")
        
        return report
    
    def run_full_audit(self):
        """Run complete audit suite"""
        print("="*60)
        print("RAN Network Audit - Starting")
        print("="*60)
        
        # Load data
        cell_sites = self.load_geojson("data/cell_sites/cell_sites.geojson")
        sectors = self.load_geojson("data/sectors/sectors.geojson")
        neighbours = self.load_geojson("data/neighbours/neighbours.geojson")
        coverage = self.load_geojson("data/coverage/coverage.geojson")
        
        # Run audits
        if cell_sites:
            self.audit_site_kpis(cell_sites)
        
        if sectors and neighbours:
            self.audit_neighbour_relations(sectors, neighbours)
        
        if coverage:
            self.audit_coverage(coverage)
        
        # Generate report
        self.generate_report()
        
        print("\n" + "="*60)
        print("RAN Network Audit - Completed")
        print("="*60)


def main():
    """Main entry point"""
    auditor = RANAuditor()
    auditor.run_full_audit()


if __name__ == "__main__":
    main()
