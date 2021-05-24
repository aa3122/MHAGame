from .models import Game, Session
from django.forms import ModelForm


class SessionForm(ModelForm):
	class Meta:
		model= Session
		fields = ('immunization_perc','EDUSmoking_perc','EDUDisease_perc','Screening_perc','TestingLab_perc','TestingPharmo_perc','AnnualPCP_perc','HospitalCare_perc','MentalHealth_perc','EmergencyCare_perc','OutPatientSurg_perc','OutPatientRadio_perc','PhysicianPCP_perc','PhysicianSpec_perc','UrgentCare_perc','HomeHealth_perc','Hospice_perc','LTAC_perc','SkilledNursing_perc','NursingHome_perc','AsstLiving_perc','IndLiving_perc','NameBrand_perc','GenDrugs_perc','SpecialtyDrugs_perc','DurableMedEqu_perc','TobTax_perc','Alcohol_perc','FattyFoods_perc','SugFoods_perc',)

		def __init__(self, user, *args, **kwargs):
			super(SessionForm, self).__init__(*args, **kwargs)