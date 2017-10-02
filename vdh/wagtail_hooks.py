from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import VetProfile, VppProfile, VetMedicineProducerProfile, VetMedicineDistributerProfile, ClinicalWorkData

class VetProfileModelAdmin(ModelAdmin):
    model = VetProfile
    menu_label = 'Vetenerian'  # ditch this to use verbose_name_plural from model
    menu_icon = 'snippet'  # change as required
    list_display = ('user',
            'first_name',
            'last_name' ,
            'kvb_reg_no',
            'email' ,
            'academic_inst',
            'program_studied',
            'index_no',
            'year_of_graduation',
            'academic_cert_reg_no',
            'any_other_certs',
            'license_no',
            'license_exp_date',
            'current_station_of_work',)
    list_filter = ('program_studied')
    search_fields = ('first_name','last_name', 'kvb_reg_no')

class VppProfileModelAdmin(ModelAdmin):
    model = VppProfile
    menu_label = 'Vet Paraprofessional'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('user',
            'first_name',
            'last_name' ,
            'kvb_reg_no',
            'email' ,
            'academic_inst',
            'program_studied',
            'index_no',
            'year_of_graduation',
            'academic_cert_reg_no',
            'any_other_certs',
            'license_no',
            'license_exp_date',
            'current_station_of_work',
            'supervising_vet')
    list_filter = ('program_studied')
    search_fields = ('first_name','last_name', 'kvb_reg_no')

class VetMedicineProducerProfileModelAdmin(ModelAdmin):
    model = VetMedicineProducerProfile
    menu_label = 'Vet Medicine Producer'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('user',
            'first_name',
            'last_name' ,
            'kvb_reg_no',
            'email' ,
            'academic_inst',
            'program_studied',
            'index_no',
            'year_of_graduation',
            'academic_cert_reg_no',
            'any_other_certs',
            'license_no',
            'license_exp_date',
            'current_station_of_work',
            'supervising_vet')
    list_filter = ('program_studied')
    search_fields = ('first_name','last_name', 'kvb_reg_no')


class VetMedicineDistributerProfileModelAdmin(ModelAdmin):
    model = VetMedicineDistributerProfile
    menu_label = 'Vet Medicine Distributer'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('user',
            'first_name',
            'last_name' ,
            'kvb_reg_no',
            'email' ,
            'academic_inst',
            'program_studied',
            'index_no',
            'year_of_graduation',
            'academic_cert_reg_no',
            'any_other_certs',
            'license_no',
            'license_exp_date',
            'current_station_of_work',
            'supervising_vet')
    list_filter = ('program_studied')
    search_fields = ('first_name','last_name', 'kvb_reg_no')


class ClinicalWorkDataFormModelAdmin(ModelAdmin):
    model = ClinicalWorkData
    menu_label = 'Vet Medicine Distributer'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('animal_species',
            'identification',
            'owner',
            'complaint',
            'diagnosis',
            'diagnostic_method_used',
            'treatment_product_used',
            'treatment_amount_used',
            'treatment_batch_no',
            'outcome_of_treatment',
            'advice_given',)
    list_filter = ('diagnosis', 'diagnostic_method_used','treatment_product_used')
    search_fields = ('first_name','last_name', 'kvb_reg_no')



class VDHAdminGroup(ModelAdminGroup):
    menu_label = 'Vet Data Hub'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (VppProfileModelAdmin,VetProfileModelAdmin,VetMedicineProducerProfileModelAdmin, VetMedicineDistributerProfileModelAdmin, ClinicalWorkDataFormModelAdmin)

# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(VDHAdminGroup)

