from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def ortho_report(request):
    json_response = {
        "resourceType": "Encounter",
        "meta": {
            "lastUpdated": "2017-08-30T15:50:36Z"
        },
        "text": {
            "status": "additional",
        },
        "status": "unknown",
        "participant":  [
            {
                "type":  [
                    {
                        "coding":  [
                            {
                                "code": "ADM",
                                "display": "Admitting"
                            }
                        ]
                    }
                ],
                "individual": {
                    "reference": "Practitioner#1"
                }
            }
        ]
    }
    return JsonResponse(json_response)



def ortho_final_report(request):
  json_response = {
    "resourceType": "ValueSet",
    "id": "c80-doc-typecodes",
    "meta": {
      "lastUpdated": "2019-10-31T22:29:23.356+00:00",
      "profile": [
        "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
      ]
    },
    "identifier": [
      {
        "system": "urn:ietf:rfc:3986",
        "value": "urn:oid:2.16.840.1.113883.3.88.12.80.47"
      }
    ],
    "version": "4.0.1",
    "title": "Document Type Value Set",
    "experimental": False,
    "publisher": "HITSP",
    "contact": [
      {
        "telecom": [
          {
            "system": "url",
            "value": "http://hl7.org/fhir"
          },
          {
            "system": "email",
            "value": "fhir@lists.hl7.org"
          }
        ]
      }
    ],
    "description": "This is the code specifying the precise type of document (e.g. Pulmonary History and  Physical, Discharge Summary, Ultrasound Report, etc.). The Document Type value set includes all LOINC  values listed in HITSP C80 Table 2-144 Document Class Value Set Definition above used for Document Class,  and all LOINC values whose SCALE is DOC in the LOINC database.",
    "copyright": "This content from LOINC® is copyright © 1995 Regenstrief Institute, Inc. and the LOINC Committee, and available at no cost under the license at http://loinc.org/terms-of-use."
  }
  return JsonResponse(json_response)