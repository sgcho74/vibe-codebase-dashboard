# Dashboard Schema

## JSON Output Structure

```json
{
  "overall": {
    "score": 0,
    "grade": "C",
    "status": "Needs standardization",
    "primary_risk": "",
    "recommended_first_action": ""
  },
  "dimensions": [
    {
      "name": "Context Readiness",
      "weight": 10,
      "score": 0,
      "weighted_score": 0,
      "status": "missing",
      "evidence": [],
      "gaps": [],
      "recommendations": []
    }
  ],
  "vibeops": {
    "confidence": {
      "score": 0,
      "status": "",
      "evidence": [],
      "gaps": []
    },
    "explainability": {
      "score": 0,
      "status": "",
      "evidence": [],
      "gaps": []
    },
    "blast_radius": {
      "score": 0,
      "status": "",
      "evidence": [],
      "gaps": []
    },
    "evidence_of_review": {
      "score": 0,
      "status": "",
      "evidence": [],
      "gaps": []
    }
  },
  "top_gaps": [],
  "red_flags": [],
  "quick_wins": [],
  "recommended_files": [],
  "recommended_skills": []
}
```
