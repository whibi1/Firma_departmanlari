class Firma:
    """Firmanın bölümleri"""

    def __init__(self, isealim: str, satinalma: str, egitim: str, muhasebe: str,hukuk: str ) -> str:
        self.isealim = isealim
        self.satinalma = satinalma
        self.egitim = egitim
        self.muhasebe=muhasebe
        self.hukuk=hukuk
    
    def get_firma(self) -> str:
        return f"Firmanın Bölümleri:\n\
            isealim: {self.isealim}\
            satinalma: {self.satinalma}\
            egitim: {self.egitim}\
            muhasebe: {self.muhasebe}\
            hukuk:{self.hukuk}"

print (
    Firma
(isealim="Gelen özgeçmişleri inceleyerek işe alım işlemleri yapar.\n",
satinalma="Ürünleri fiyat kalite açısından inceleyerek en ideal ürünleri satın alır.\n",
egitim="Personele ihtiyaç dahilinde eğitim planlaması ve uygulaması yapar.\n",
muhasebe="Firmanın finansal kaynaklarının kaydını tutar anormal durumları rapor eder.\n",
hukuk="Firmanın hukuksal işlemlerini yürütür, davaları takip eder.\n").get_firma()
)

    