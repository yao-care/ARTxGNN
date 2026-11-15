/**
 * ARTxGNN Drug-Drug Interaction Checker
 *
 * Client-side DDI checking with 15 built-in curated rules (DDInter consulted as a reference; not a full database lookup).
 * Provides real-time interaction alerts for drug repurposing candidates.
 *
 * @author ARTxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  const CONFIG = {
    // This site does not publish /data/ddi-index.json; only the curated rules
    // below are used. Set a URL here once such a file exists.
    ddiDataUrl: null,
    maxAlerts: 10
  };

  // Severity levels with priority (higher = more severe)
  const SEVERITY = {
    'Major': { priority: 3, class: 'ddi-major', label: 'Grave' },
    'Moderate': { priority: 2, class: 'ddi-moderate', label: 'Moderada' },
    'Minor': { priority: 1, class: 'ddi-minor', label: 'Leve' }
  };

  // 15 built-in high-priority DDI rules (hand-curated, DDInter consulted as a reference)
  // Format: { drug1: [synonym list], drug2: [synonym list], severity, summary, detail }
  const CURATED_DDI_RULES = [
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['ibuprofen', 'advil', 'motrin', 'brufen']
      ],
      severity: 'Major',
      summary: 'Warfarina + Ibuprofeno: mayor riesgo de hemorragia',
      detail: 'Los AINE inhiben la función plaquetaria y pueden potenciar el efecto anticoagulante de la warfarina, lo que aumenta de forma importante el riesgo de hemorragia digestiva.',
      recommendation: 'Use paracetamol en su lugar o añada un IBP como protección gástrica.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['aspirin', 'acetylsalicylic acid']
      ],
      severity: 'Major',
      summary: 'Warfarina + Ácido acetilsalicílico: mayor riesgo de hemorragia',
      detail: 'Ambos afectan a la hemostasia; su uso conjunto aumenta mucho el riesgo de hemorragia.',
      recommendation: 'Si la combinación es necesaria, use ácido acetilsalicílico a dosis bajas y vigile estrechamente el INR.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['naproxen', 'aleve', 'naprosyn']
      ],
      severity: 'Major',
      summary: 'Warfarina + Naproxeno: mayor riesgo de hemorragia',
      detail: 'Combinar naproxeno con warfarina aumenta el riesgo de hemorragia digestiva y de otras hemorragias.',
      recommendation: 'Use paracetamol para el dolor en su lugar.'
    },
    {
      drugs: [
        ['metformin', 'glucophage'],
        ['iodixanol', 'visipaque', 'iopamidol', 'isovue', 'contrast']
      ],
      severity: 'Major',
      summary: 'Metformina + contrastes yodados: riesgo de acidosis láctica',
      detail: 'Los contrastes pueden causar lesión renal aguda, con acumulación de metformina y acidosis láctica.',
      recommendation: 'Suspenda la metformina 48 horas antes del procedimiento y reanúdela solo tras confirmar que la función renal es normal.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['clarithromycin', 'biaxin', 'klacid']
      ],
      severity: 'Major',
      summary: 'Colchicina + Claritromicina: riesgo de toxicidad',
      detail: 'La claritromicina es un inhibidor potente del CYP3A4 y aumenta mucho las concentraciones de colchicina.',
      recommendation: 'Evite la combinación o reduzca sustancialmente la dosis de colchicina.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['ritonavir', 'norvir', 'cobicistat', 'tybost']
      ],
      severity: 'Major',
      summary: 'Colchicina + inhibidores de la proteasa del VIH: riesgo de toxicidad grave',
      detail: 'Los inhibidores de la proteasa del VIH aumentan notablemente las concentraciones de colchicina y pueden causar toxicidad mortal.',
      recommendation: 'Contraindicado en pacientes con insuficiencia renal o hepática.'
    },
    {
      drugs: [
        ['simvastatin', 'zocor'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Simvastatina + Amiodarona: riesgo de miopatía',
      detail: 'La amiodarona aumenta las concentraciones de simvastatina y eleva el riesgo de rabdomiólisis.',
      recommendation: 'No supere 20 mg/día de simvastatina o cambie a otra estatina.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['tramadol', 'ultram']
      ],
      severity: 'Major',
      summary: 'ISRS + Tramadol: riesgo de síndrome serotoninérgico',
      detail: 'Ambos aumentan la actividad serotoninérgica; su uso conjunto puede causar un síndrome serotoninérgico potencialmente mortal.',
      recommendation: 'Vigile estrechamente los síntomas (hipertermia, mioclonías, alteración del estado mental) y considere otro analgésico.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['linezolid', 'zyvox']
      ],
      severity: 'Major',
      summary: 'ISRS + Linezolid: riesgo de síndrome serotoninérgico',
      detail: 'El linezolid es un inhibidor de la MAO; combinarlo con un ISRS es muy peligroso.',
      recommendation: 'Evite la combinación. Si el linezolid es necesario, suspenda el ISRS y respete un periodo de lavado adecuado.'
    },
    {
      drugs: [
        ['amiodarone', 'cordarone'],
        ['moxifloxacin', 'avelox']
      ],
      severity: 'Major',
      summary: 'Amiodarona + Moxifloxacino: riesgo de prolongación del QT',
      detail: 'Ambos pueden prolongar el intervalo QT; su uso conjunto aumenta el riesgo de torsade de pointes.',
      recommendation: 'Evite la combinación o vigile estrechamente el ECG.'
    },
    {
      drugs: [
        ['digoxin', 'lanoxin'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Digoxina + Amiodarona: riesgo de toxicidad por digoxina',
      detail: 'La amiodarona aumenta las concentraciones de digoxina en aproximadamente un 70%.',
      recommendation: 'Al iniciar la amiodarona, reduzca a la mitad la dosis de digoxina y vigile sus concentraciones.'
    },
    {
      drugs: [
        ['clopidogrel', 'plavix'],
        ['omeprazole', 'prilosec', 'esomeprazole', 'nexium']
      ],
      severity: 'Moderate',
      summary: 'Clopidogrel + IBP: menor efecto antiagregante',
      detail: 'El omeprazol inhibe el CYP2C19 y reduce la conversión del clopidogrel en su metabolito activo.',
      recommendation: 'Considere pantoprazol o un antagonista H2 en su lugar.'
    },
    {
      drugs: [
        ['lithium', 'lithobid'],
        ['ibuprofen', 'advil', 'naproxen', 'aleve', 'diclofenac']
      ],
      severity: 'Major',
      summary: 'Litio + AINE: riesgo de toxicidad por litio',
      detail: 'Los AINE reducen la excreción renal de litio y aumentan sus concentraciones.',
      recommendation: 'Evite la combinación o vigile estrechamente las concentraciones de litio.'
    },
    {
      drugs: [
        ['potassium', 'k-dur', 'klor-con'],
        ['spironolactone', 'aldactone', 'eplerenone', 'inspra']
      ],
      severity: 'Major',
      summary: 'Suplementos de potasio + diuréticos ahorradores de potasio: riesgo de hiperpotasemia',
      detail: 'Ambos elevan el potasio sérico; su uso conjunto puede causar una hiperpotasemia potencialmente mortal.',
      recommendation: 'Controle periódicamente el potasio sérico y evite los suplementos de potasio concomitantes.'
    },
    {
      drugs: [
        ['methotrexate', 'trexall'],
        ['trimethoprim', 'bactrim', 'septra', 'sulfamethoxazole']
      ],
      severity: 'Major',
      summary: 'Metotrexato + TMP-SMX: riesgo de mielosupresión',
      detail: 'Ambos inhiben el metabolismo del folato; su uso conjunto aumenta el riesgo de mielosupresión y mucositis.',
      recommendation: 'Evite la combinación o asegure un aporte adecuado de folato y vigile estrechamente el hemograma.'
    }
  ];

  let ddiIndex = null;
  let isLoaded = false;

  /**
   * Load DDI index data
   */
  async function loadDDIIndex() {
    if (isLoaded) return;
    if (!CONFIG.ddiDataUrl) {
      isLoaded = true;
      return;
    }

    try {
      const response = await fetch(CONFIG.ddiDataUrl);
      if (response.ok) {
        ddiIndex = await response.json();
        isLoaded = true;
        console.log('DDI index loaded:', ddiIndex?.count || 0, 'interactions');
      }
    } catch (error) {
      console.warn('DDI index not available, using curated rules only');
      isLoaded = true;
    }
  }

  /**
   * Normalize drug name for comparison
   */
  function normalizeDrugName(name) {
    if (!name) return '';
    return name.toLowerCase()
      .replace(/\s+/g, ' ')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Check if a drug name matches any of the synonyms
   */
  function matchesDrug(drugName, synonyms) {
    const normalized = normalizeDrugName(drugName);
    return synonyms.some(syn => {
      const normalizedSyn = normalizeDrugName(syn);
      return normalized.includes(normalizedSyn) || normalizedSyn.includes(normalized);
    });
  }

  /**
   * Check for DDI between two drugs using curated rules
   */
  function checkCuratedDDI(drug1, drug2) {
    const alerts = [];

    for (const rule of CURATED_DDI_RULES) {
      const [drugGroup1, drugGroup2] = rule.drugs;

      // Check if drug1 matches group1 and drug2 matches group2, or vice versa
      if (
        (matchesDrug(drug1, drugGroup1) && matchesDrug(drug2, drugGroup2)) ||
        (matchesDrug(drug1, drugGroup2) && matchesDrug(drug2, drugGroup1))
      ) {
        alerts.push({
          drug1: drug1,
          drug2: drug2,
          severity: rule.severity,
          severityInfo: SEVERITY[rule.severity],
          summary: rule.summary,
          detail: rule.detail,
          recommendation: rule.recommendation,
          source: 'Reglas DDI integradas de ARTxGNN (15 reglas seleccionadas; no es una consulta completa de DDInter)'
        });
      }
    }

    return alerts;
  }

  /**
   * Check DDI for a list of medications
   * @param {string[]} medications - Array of medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkInteractions(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const allAlerts = [];
    const seen = new Set();

    // Check all pairs
    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const drug1 = medications[i];
        const drug2 = medications[j];
        const pairKey = [drug1, drug2].sort().join('|');

        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const alerts = checkCuratedDDI(drug1, drug2);
        allAlerts.push(...alerts);
      }
    }

    // Sort by severity (highest first) and limit
    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority)
      .slice(0, CONFIG.maxAlerts);
  }

  /**
   * Check if a new drug has interactions with existing medications
   * @param {string} newDrug - The new drug to check
   * @param {string[]} currentMeds - Array of current medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkNewDrug(newDrug, currentMeds) {
    if (!newDrug || !currentMeds || currentMeds.length === 0) {
      return [];
    }

    const allAlerts = [];

    for (const currentDrug of currentMeds) {
      const alerts = checkCuratedDDI(newDrug, currentDrug);
      allAlerts.push(...alerts);
    }

    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority);
  }

  /**
   * Format alerts as HTML for display
   */
  function formatAlertsHTML(alerts) {
    if (!alerts || alerts.length === 0) {
      return '<div class="ddi-no-alerts">No se encontraron alertas de interacciones</div>';
    }

    let html = '<div class="ddi-alerts">';

    alerts.forEach((alert, index) => {
      html += `
        <div class="ddi-alert ${alert.severityInfo.class}">
          <div class="ddi-alert-header">
            <span class="ddi-severity-badge">${alert.severityInfo.label}</span>
            <span class="ddi-summary">${escapeHtml(alert.summary)}</span>
          </div>
          <div class="ddi-alert-body">
            <p class="ddi-detail">${escapeHtml(alert.detail)}</p>
            <p class="ddi-recommendation"><strong>Recomendación:</strong> ${escapeHtml(alert.recommendation)}</p>
          </div>
          <div class="ddi-alert-footer">
            <span class="ddi-source">Fuente: ${escapeHtml(alert.source)}</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    return html;
  }

  /**
   * Format alerts for CDS Hooks response
   */
  function formatForCDSHooks(alerts) {
    return alerts.map((alert, index) => ({
      uuid: `ddi-alert-${index}`,
      summary: alert.summary,
      indicator: alert.severity === 'Major' ? 'critical' : alert.severity === 'Moderate' ? 'warning' : 'info',
      detail: `${alert.detail}\n\nRecomendación: ${alert.recommendation}`,
      source: {
        label: 'ARTxGNN DDI Checker',
        url: 'https://artxgnn.yao.care/'
      }
    }));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.TwTxGNN = global.TwTxGNN || {};
  global.TwTxGNN.DDIChecker = {
    load: loadDDIIndex,
    checkInteractions: checkInteractions,
    checkNewDrug: checkNewDrug,
    formatAlertsHTML: formatAlertsHTML,
    formatForCDSHooks: formatForCDSHooks,
    SEVERITY: SEVERITY
  };

  // Auto-load when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadDDIIndex);
  } else {
    loadDDIIndex();
  }

})(typeof window !== 'undefined' ? window : this);
