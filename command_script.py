__rethrow_casa_exceptions = True #standard
context = h_init() #standard
context.set_state('ProjectSummary', 'proposal_code', 'VLASS') #standard
context.set_state('ProjectSummary', 'proposal_title', 'unknown') #standard
context.set_state('ProjectSummary', 'piname', 'unknown') #standard
context.set_state('ProjectSummary', 'observatory', 'Karl G. Jansky Very Large Array') #standard
context.set_state('ProjectSummary', 'telescope', 'EVLA') #standard
context.set_state('ProjectStructure', 'ppr_file', 'PPR.xml') #standard
context.set_state('ProjectStructure', 'recipe_name', 'hifv_vlassSEIP') #standard
try:
    hifv_importdata(nocopy=True, vis=['example.ms'], session=['session_1'])
    hif_editimlist(parameter_file='SEIP_parameter.list')
    hif_transformimagedata(datacolumn='data', clear_pointing=False, modify_weights=True, wtmode='nyq')
    hifv_vlassmasking(maskingmode='vlass-se-tier-1', vlass_ql_database='/data/astrolab/Carlson/Astro/VLASS_Data/VLASS1Q.fits')
    hif_makeimages(hm_masking='manual')
    hifv_checkflag(checkflagmode='vlass-imaging')
    hifv_statwt(statwtmode='VLASS-SE', datacolumn='residual_data')
    hifv_selfcal(selfcalmode='VLASS-SE')
    hif_editimlist(parameter_file='SEIP_parameter.list')
    hif_makeimages(hm_masking='manual')
    hif_editimlist(parameter_file='SEIP_parameter.list')
    hifv_vlassmasking(maskingmode='vlass-se-tier-2')
    hif_makeimages(hm_masking='manual')
    hifv_pbcor(pipelinemode="automatic")
    hif_makermsimages(pipelinemode="automatic")
    hif_makecutoutimages(pipelinemode="automatic")
    hif_analyzealpha(pipelinemode="automatic")
    hifv_exportvlassdata(pipelinemode="automatic")
finally:
    h_save()