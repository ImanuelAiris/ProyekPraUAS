from django.shortcuts import render
from rest_framework.response import Response
import paho.mqtt.client as mqtt

from .serializers import *
from .models import *
from .machinelearning import *

machinelearning1 = mlpotong()
machinelearning2 = mljahit()
machinelearning3 = mlbenang()
machinelearning4 = mlbahan()
machinelearning5 = mlkain()
machinelearning6 = mlketahanan()
machinelearning7 = mlkualitas()
machinelearning8 = mlpenghalusan()
machinelearning9 = mlpembersihan()
machinelearning10 = mltailoring()
machinelearning11 = mlteksitl()
machinelearning12 = mlfinishing()
machinelearning13 = mlclothing()

def webview(request):
    """A view of all bands."""
    view1 = Sistem1.objects.all().values()
    view2 = Sistem2.objects.all().values()
    view3 = Sistem3.objects.all().values()
    view4 = Sistem4.objects.all().values()
    view5 = Sistem5.objects.all().values()
    view6 = Sistem6.objects.all().values()
    view7 = Sistem7.objects.all().values()
    view8 = Sistem8.objects.all().values()
    view9 = Sistem9.objects.all().values()

    act1 = Aktuator.objects.filter(name__icontains='gunting')
    act2 = Aktuator.objects.filter(name__icontains='jahitan')
    act3 = Aktuator.objects.filter(name__icontains='benang')
    act4 = Aktuator.objects.filter(name__icontains='bahan')
    act5 = Aktuator.objects.filter(name__icontains='kain')
    act6 = Aktuator.objects.filter(name__icontains='ketahanan')
    act7 = Aktuator.objects.filter(name__icontains='kualitas')
    act8 = Aktuator.objects.filter(name__icontains='kehalusan')
    act9 = Aktuator.objects.filter(name__icontains='kebersihan')
    act10 = Aktuator.objects.filter(name__icontains='hasiljahit')
    act11 = Aktuator.objects.filter(name__icontains='hasiltekstil')
    act12 = Aktuator.objects.filter(name__icontains='finishing')
    act13 = Aktuator.objects.filter(name__icontains='clothing')
    return render(request, 'webview.html', {'views1': view1, 'views2':view2, 'views3':view3, 'views4':view4, 'views5':view5, 'views6':view6, 'views7':view7, 'views8':view8, 'views9':view9, 
                                             'views_act1':act1, 'views_act2':act2, 'views_act3':act3, 'views_act4':act4, 'views_act5':act5, 'views_act6':act6, 'views_act7':act7, 'views_act8':act8, 'views_act9':act9, 'views_act10':act10, 'views_act11':act11, 'views_act12':act12, 'views_act13':act13})

def actuator_prediction1():
    tekanan = Sistem1.objects.get(name="tekanan").value
    jarak = Sistem1.objects.get(name="jarak").value
    tachometer = Sistem1.objects.get(name="tachometer").value
    aktuator1 = machinelearning1.hitungml(int(tekanan), int(jarak), int(tachometer))
    data_act1 = {
        'value': aktuator1
    }
    act1 = Aktuator.objects.get(name="gunting")
    serializer = AktuatorSerializer(act1, data=data_act1, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction2():
    suhu = Sistem2.objects.get(name="suhu").value
    optik = Sistem2.objects.get(name="optik").value
    kelembaban = Sistem2.objects.get(name="kelembaban").value
    aktuator2 = machinelearning2.hitungml(int(suhu), int(optik), int(kelembaban))
    data_act2 = {
        'value': aktuator2
    }
    act2 = Aktuator.objects.get(name="jahitan")
    serializer = AktuatorSerializer(act2, data=data_act2, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction3():
    penggerakan = Sistem3.objects.get(name="penggerakan").value
    suara = Sistem3.objects.get(name="suara").value
    getaran = Sistem3.objects.get(name="getaran").value
    aktuator3 = machinelearning3.hitungml(int(penggerakan), int(suara), int(getaran))
    data_act3 = {
        'value': aktuator3
    }
    act3 = Aktuator.objects.get(name="benang")
    serializer = AktuatorSerializer(act3, data=data_act3, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction4():
    kapas = Sistem4.objects.get(name="kapas").value
    benang = Sistem4.objects.get(name="benang").value
    poliester = Sistem4.objects.get(name="poliester").value
    aktuator4 = machinelearning4.hitungml(int(kapas), int(benang), int(poliester))
    data_act4 = {
        'value': aktuator4
    }
    act4 = Aktuator.objects.get(name="bahan")
    serializer = AktuatorSerializer(act4, data=data_act4, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction5():
    kain = Sistem5.objects.get(name="kain").value
    pemintalan = Sistem5.objects.get(name="pemintalan").value
    pencelupan = Sistem5.objects.get(name="pencelupan").value
    aktuator5 = machinelearning5.hitungml(int(kain), int(pemintalan), int(pencelupan))
    data_act5 = {
        'value': aktuator5
    }
    act5 = Aktuator.objects.get(name="kain")
    serializer = AktuatorSerializer(act5, data=data_act5, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction6():
    tarik = Sistem6.objects.get(name="tarik").value
    spektrofotometer = Sistem6.objects.get(name="spektrofotometer").value
    kerutan = Sistem6.objects.get(name="kerutan").value
    aktuator6 = machinelearning6.hitungml(int(tarik), int(spektrofotometer), int(kerutan))
    data_act6 = {
        'value': aktuator6
    }
    act6 = Aktuator.objects.get(name="ketahanan")
    serializer = AktuatorSerializer(act6, data=data_act6, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction7():
    label = Sistem7.objects.get(name="label").value
    warna = Sistem7.objects.get(name="warna").value
    cacat = Sistem7.objects.get(name="cacat").value
    aktuator7 = machinelearning7.hitungml(int(label), int(warna), int(cacat))
    data_act7 = {
        'value': aktuator7
    }
    act7 = Aktuator.objects.get(name="kualitas")
    serializer = AktuatorSerializer(act7, data=data_act7, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction8():
    panas = Sistem8.objects.get(name="panas").value
    penghalus = Sistem8.objects.get(name="penghalus").value
    kimia = Sistem8.objects.get(name="kimia").value
    aktuator8 = machinelearning8.hitungml(int(panas), int(penghalus), int(kimia))
    data_act8 = {
        'value': aktuator8
    }
    act8 = Aktuator.objects.get(name="kehalusan")
    serializer = AktuatorSerializer(act8, data=data_act8, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction9():
    bau = Sistem9.objects.get(name="bau").value
    softener = Sistem9.objects.get(name="softener").value
    kotoran = Sistem9.objects.get(name="kotoran").value
    aktuator9 = machinelearning9.hitungml(int(bau), int(softener), int(kotoran))
    data_act9 = {
        'value': aktuator9
    }
    act9 = Aktuator.objects.get(name="kebersihan")
    serializer = AktuatorSerializer(act9, data=data_act9, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction10():
    gunting = Aktuator.objects.get(name="gunting").value
    jahitan = Aktuator.objects.get(name="jahitan").value
    benang = Aktuator.objects.get(name="benang").value
    aktuator10 = machinelearning10.hitungml(float(gunting), float(jahitan), float(benang))
    data_act10 = {
        'value': aktuator10
    }
    act10 = Aktuator.objects.get(name="hasiljahit")
    serializer = AktuatorSerializer(act10, data=data_act10, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction11():
    bahan = Aktuator.objects.get(name="bahan").value
    kain = Aktuator.objects.get(name="kain").value
    ketahanan = Aktuator.objects.get(name="ketahanan").value
    aktuator11 = machinelearning11.hitungml(float(bahan), float(kain), float(ketahanan))
    data_act11 = {
        'value': aktuator11
    }
    act11 = Aktuator.objects.get(name="hasiltekstil")
    serializer = AktuatorSerializer(act11, data=data_act11, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction12():
    kualitas = Aktuator.objects.get(name="kualitas").value
    kehalusan = Aktuator.objects.get(name="kehalusan").value
    kebersihan = Aktuator.objects.get(name="kebersihan").value
    aktuator12 = machinelearning12.hitungml(float(kualitas), float(kehalusan), float(kebersihan))
    data_act12 = {
        'value': aktuator12
    }
    act12 = Aktuator.objects.get(name="finishing")
    serializer = AktuatorSerializer(act12, data=data_act12, partial=True)
    if serializer.is_valid():
        serializer.save()

def actuator_prediction13():
    hasiljahit = Aktuator.objects.get(name="hasiljahit").value
    finishing = Aktuator.objects.get(name="finishing").value
    hasiltekstil = Aktuator.objects.get(name="hasiltekstil").value
    aktuator13 = machinelearning13.hitungml(float(hasiljahit), float(finishing), float(hasiltekstil))
    data_act13 = {
        'value': aktuator13
    }
    act13 = Aktuator.objects.get(name="clothing")
    serializer = AktuatorSerializer(act13, data=data_act13, partial=True)
    if serializer.is_valid():
        serializer.save()

# ---------------------------------------------------------------------

def on_message_tekanan(client, userdata, msg):
    tekanan = Sistem1.objects.get(name="tekanan")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem1Serializer(tekanan, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new tekanan data ', msg.payload.decode('utf-8'))    
    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_jarak(client, userdata, msg):
    jarak = Sistem1.objects.get(name="jarak")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem1Serializer(jarak, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new jarak data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_tachometer(client, userdata, msg):
    tachometer = Sistem1.objects.get(name="tachometer")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem1Serializer(tachometer, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new tachometer data ', msg.payload.decode('utf-8'))    
    actuator_prediction1()
    return Response({"value": msg.payload.decode('utf-8')})

# ---------------------------------------------------------------------

def on_message_suhu(client, userdata, msg):
    suhu = Sistem2.objects.get(name="suhu")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem2Serializer(suhu, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new suhu data ', msg.payload.decode('utf-8'))    
    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_optik(client, userdata, msg):
    optik = Sistem2.objects.get(name="optik")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem2Serializer(optik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new optik data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_kelembaban(client, userdata, msg):
    kelembaban = Sistem2.objects.get(name="kelembaban")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem2Serializer(kelembaban, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new kelembaban data ', msg.payload.decode('utf-8'))    
    actuator_prediction2()
    return Response({"value": msg.payload.decode('utf-8')})

# ---------------------------------------------------------------------

def on_message_penggerakan(client, userdata, msg):
    penggerakan = Sistem3.objects.get(name="penggerakan")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem3Serializer(penggerakan, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new penggerakan data ', msg.payload.decode('utf-8'))    
    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_suara(client, userdata, msg):
    suara = Sistem3.objects.get(name="suara")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem3Serializer(suara, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new suara data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_getaran(client, userdata, msg):
    getaran = Sistem3.objects.get(name="getaran")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem3Serializer(getaran, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new getaran data ', msg.payload.decode('utf-8'))    
    actuator_prediction3()
    actuator_prediction10()
    return Response({"value": msg.payload.decode('utf-8')})

# ---------------------------------------------------------------------

def on_message_kapas(client, userdata, msg):
    kapas = Sistem4.objects.get(name="kapas")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem4Serializer(kapas, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new kapas data ', msg.payload.decode('utf-8'))    
    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_benang(client, userdata, msg):
    benang = Sistem4.objects.get(name="benang")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem4Serializer(benang, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new benang data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_poliester(client, userdata, msg):
    poliester = Sistem4.objects.get(name="poliester")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem4Serializer(poliester, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new poliester data ', msg.payload.decode('utf-8'))    
    actuator_prediction4()
    return Response({"value": msg.payload.decode('utf-8')})

# ---------------------------------------------------------------------

def on_message_kain(client, userdata, msg):
    kain = Sistem5.objects.get(name="kain")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem5Serializer(kain, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new kain data ', msg.payload.decode('utf-8'))    
    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_pemintalan(client, userdata, msg):
    pemintalan = Sistem5.objects.get(name="pemintalan")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem5Serializer(pemintalan, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new pemintalan data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_pencelupan(client, userdata, msg):
    pencelupan = Sistem5.objects.get(name="pencelupan")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem5Serializer(pencelupan, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new pencelupan data ', msg.payload.decode('utf-8'))    
    actuator_prediction5()
    return Response({"value": msg.payload.decode('utf-8')})

# ---------------------------------------------------------------------

def on_message_tarik(client, userdata, msg):
    tarik = Sistem6.objects.get(name="tarik")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem6Serializer(tarik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new tarik data ', msg.payload.decode('utf-8'))    
    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_spektrofotometer(client, userdata, msg):
    spektrofotometer = Sistem6.objects.get(name="spektrofotometer")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem6Serializer(spektrofotometer, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new spektrofotometer data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_kerutan(client, userdata, msg):
    kerutan = Sistem6.objects.get(name="kerutan")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem6Serializer(kerutan, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new kerutan data ', msg.payload.decode('utf-8'))    
    actuator_prediction6()
    actuator_prediction11()
    return Response({"value": msg.payload.decode('utf-8')})

# ---------------------------------------------------------------------

def on_message_label(client, userdata, msg):
    label = Sistem7.objects.get(name="label")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem7Serializer(label, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new label data ', msg.payload.decode('utf-8'))    
    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_warna(client, userdata, msg):
    warna = Sistem7.objects.get(name="warna")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem7Serializer(warna, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new warna data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_cacat(client, userdata, msg):
    cacat = Sistem7.objects.get(name="cacat")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem7Serializer(cacat, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new cacat data ', msg.payload.decode('utf-8'))    
    actuator_prediction7()
    return Response({"value": msg.payload.decode('utf-8')})

# ---------------------------------------------------------------------

def on_message_panas(client, userdata, msg):
    panas = Sistem8.objects.get(name="panas")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem8Serializer(panas, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new panas data ', msg.payload.decode('utf-8'))    
    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_penghalus(client, userdata, msg):
    penghalus = Sistem8.objects.get(name="penghalus")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem8Serializer(penghalus, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new penghalus data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_kimia(client, userdata, msg):
    kimia = Sistem8.objects.get(name="kimia")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem8Serializer(kimia, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new kimia data ', msg.payload.decode('utf-8'))    
    actuator_prediction8()
    return Response({"value": msg.payload.decode('utf-8')})

# ---------------------------------------------------------------------

def on_message_bau(client, userdata, msg):
    bau = Sistem9.objects.get(name="bau")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem9Serializer(bau, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new bau data ', msg.payload.decode('utf-8'))    
    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_softener(client, userdata, msg):
    softener = Sistem9.objects.get(name="softener")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem9Serializer(softener, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new softener data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_kotoran(client, userdata, msg):
    kotoran = Sistem9.objects.get(name="kotoran")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem9Serializer(kotoran, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new kotoran data ', msg.payload.decode('utf-8'))    
    actuator_prediction9()
    actuator_prediction12()
    actuator_prediction13()
    return Response({"value": msg.payload.decode('utf-8')})

# ---------------------------------------------------------------------

client = mqtt.Client("clothing_industry_app")

client.message_callback_add('ci/tekanan', on_message_tekanan)
client.message_callback_add('ci/jarak', on_message_jarak)
client.message_callback_add('ci/tachometer', on_message_tachometer)

client.message_callback_add('ci/suhu', on_message_suhu)
client.message_callback_add('ci/optik', on_message_optik)
client.message_callback_add('ci/kelembaban', on_message_kelembaban)

client.message_callback_add('ci/penggerakan', on_message_penggerakan)
client.message_callback_add('ci/suara', on_message_suara)
client.message_callback_add('ci/getaran', on_message_getaran)

client.message_callback_add('ci/kapas', on_message_kapas)
client.message_callback_add('ci/benang', on_message_benang)
client.message_callback_add('ci/poliester', on_message_poliester)

client.message_callback_add('ci/kain', on_message_kain)
client.message_callback_add('ci/pemintalan', on_message_pemintalan)
client.message_callback_add('ci/pencelupan', on_message_pencelupan)

client.message_callback_add('ci/tarik', on_message_tarik)
client.message_callback_add('ci/spektrofotometer', on_message_spektrofotometer)
client.message_callback_add('ci/kerutan', on_message_kerutan)

client.message_callback_add('ci/label', on_message_label)
client.message_callback_add('ci/warna', on_message_warna)
client.message_callback_add('ci/cacat', on_message_cacat)

client.message_callback_add('ci/panas', on_message_panas)
client.message_callback_add('ci/penghalus', on_message_penghalus)
client.message_callback_add('ci/kimia', on_message_kimia)

client.message_callback_add('ci/bau', on_message_bau)
client.message_callback_add('ci/softener', on_message_softener)
client.message_callback_add('ci/kotoran', on_message_kotoran)

client.connect('localhost', 1883)
client.loop_start()
client.subscribe('ci/#')
