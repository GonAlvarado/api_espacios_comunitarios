from django.db import models

class DiaDb(models.Model):
    dia = models.CharField(verbose_name="Dia", max_length=10, null=False, blank=False)

    class Meta:
        db_table = "Dias"
        verbose_name = "Dia"
        verbose_name_plural = "Dias"

    def __str__(self) -> str:
        return self.dia
    
class HorarioDb(models.Model):
    horario = models.CharField(verbose_name="Horario", max_length=10, null=False, blank=False)

    class Meta:
        db_table = "Horarios"
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    def __str__(self) -> str:
        return self.horario

class ReferenteDb(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False)
    apellido = models.CharField(verbose_name="Apellido", max_length=100, null=False)
    telefono = models.CharField(verbose_name="Telefono", max_length=20, null=False)
    dni = models.IntegerField(verbose_name="Dni", null=False)

    class Meta:
        db_table = "Referentes"
        verbose_name = "Referente"
        verbose_name_plural = "Referentes"

    def __str__(self) -> str:
        return self.nombre + " " + self.apellido

class EspacioDb(models.Model):
    tipo = models.CharField(verbose_name="Tipo", max_length=20, null=False)
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False)
    direccion = models.CharField(verbose_name="Direccion", max_length=100, null=False)
    coordenadas = models.CharField(verbose_name="Coordenadas", max_length=100, null=False)
    dia = models.ManyToManyField(DiaDb, verbose_name="Dia")
    horario = models.ManyToManyField(HorarioDb, verbose_name="Horario")
    barrio = models.CharField(verbose_name="Barrio", max_length=100, null=False)
    tarjeta = models.BooleanField(verbose_name="Tarjeta", null=False, blank=False)
    asistencia = models.IntegerField(verbose_name="Asistencia", null=False)
    referente_fk = models.ForeignKey(ReferenteDb, on_delete=models.CASCADE)

    class Meta:
        db_table = "Espacios comunitarios"
        verbose_name = "Espacio comunitario"
        verbose_name_plural = "Espacios comunitarios"

    def __str__(self) -> str:
        return self.nombre

class RetiroDb(models.Model):
    fecha = models.DateField(verbose_name="Fecha", null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripcion", max_length=500, null=False, blank=False)
    agente = models.CharField(verbose_name="Agente", max_length=100, null=False, blank=False)
    espacio_fk = models.ForeignKey(EspacioDb, on_delete=models.CASCADE, related_name="retiros")

    class Meta:
        db_table = "Retiros"
        verbose_name = "Retiro"
        verbose_name_plural = "Retiros"

    def __str__(self) -> str:
        return "Fecha: " + self.fecha.strftime('%d-%m-%Y') + ", Descripcion: " + self.descripcion