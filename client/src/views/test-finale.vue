<template>
    <div class="conclusion col-10">
        <p class="text-success mb-3">
            Внимание! Результаты и интерпретации, полученные без участия специалистов, не следует воспринимать слишком
            серьезно. Диагностическую ценность имеют только исследования, проведенные <span
            class="text-primary">профессиональным психологом</span>.
        </p>
        <p class="testCard testCard-point testCard-background conclusion__link fw-bold">
            Ссылка на результаты теста: <span class="fw-light">Ссылка</span>
        </p>
        <div class="tab mw-100 p-5 mb-4">
            <p class="h2 fw-bold mb-5">Индекс агрессии</p>

            <div class="text-secondary mb-4">
                <div class="w-100">
                    <div class="d-flex justify-content-between mb-2">
                        <div class="d-flex gap-2">
                            <span
                                v-for="point in 22"
                                :key="point+Date.now()"
                                :class="point>5?'conclusion__point':'conclusion__point conclusion__point--active'"
                            />
                        </div>
                        <p class="h3 fw-bolder">2</p>
                    </div>
                </div>
                <p class="h3 text-primary fw-medium">Низкий</p>
            </div>
            <div class="text-secondary mb-2">
                <div class="w-100">
                    <div class="d-flex justify-content-between mb-2">
                        <div class="d-flex gap-2">
                            <span
                                v-for="point in 22"
                                :key="point+Date.now()"
                                :class="point>5?'conclusion__point':'conclusion__point conclusion__point--active'"
                            />
                        </div>
                        <p class="h3 fw-bolder">2</p>
                    </div>
                </div>
                <p class="h3 text-primary fw-medium">Повышенный</p>
            </div>



            <div class="d-flex justify-content-between align-items-center text-secondary mb-3">
                Физическая агрессия
                <div class="d-flex gap-2">
                    <span
                        v-for="point in 22"
                        :key="point+Date.now()"
                        :class="point>5?'conclusion__point':'conclusion__point conclusion__point--active'"></span>
                </div>
                <p class="h3 fw-bolder">2</p>
            </div>
            <div class="d-flex justify-content-between align-items-center text-secondary mb-3">
                Физическая агрессия
                <div class="d-flex gap-2">
                    <span
                        v-for="point in 22"
                        :key="point+Date.now()"
                        :class="point>5?'conclusion__point':'conclusion__point conclusion__point--active'"></span>
                </div>
                <p class="h3 fw-bolder">2</p>
            </div>
            <div class="d-flex justify-content-between align-items-center text-secondary mb-3">
                Физическая агрессия
                <div class="d-flex gap-2">
                    <span
                        v-for="point in 22"
                        :key="point+Date.now()"
                        :class="point>5?'conclusion__point':'conclusion__point conclusion__point--active'"></span>
                </div>
                <p class="h3 fw-bolder">2</p>
            </div>
            <div class="d-flex justify-content-between align-items-center text-secondary mb-3">
                Физическая агрессия
                <div class="d-flex gap-2">
                    <span
                        v-for="point in 22"
                        :key="point+Date.now()"
                        :class="point>5?'conclusion__point':'conclusion__point conclusion__point--active'"></span>
                </div>
                <p class="h3 fw-bolder">2</p>
            </div>
            <div class="d-flex justify-content-between align-items-center text-secondary mb-3">
                Физическая агрессия
                <div class="d-flex gap-2">
                    <span
                        v-for="point in 22"
                        :key="point+Date.now()"
                        :class="point>5?'conclusion__point':'conclusion__point conclusion__point--active'"></span>
                </div>
                <p class="h3 fw-bolder">2</p>
            </div>
            <div class="d-flex justify-content-between align-items-center text-secondary mb-3">
                Физическая агрессия
                <div class="d-flex gap-2">
                    <span
                        v-for="point in 22"
                        :key="point+Date.now()"
                        :class="point>5?'conclusion__point':'conclusion__point conclusion__point--active'"></span>
                </div>
                <p class="h3 fw-bolder">2</p>
            </div>


        </div>
        <h2 class="mb-4">Содержательная интерпретация</h2>
        <p class="testCard testCard-point py-1 mb-4">
            • Ситуативная или реактивная тревожность как состояние характеризуется субъективно переживаемыми эмоциями:
            напряжением, беспокойством, озабоченностью, нервозностью. Это состояние отличается неустойчивостью во
            времени и различной интенсивностью в зависимости от силы воздействия стрессовой ситуации. Таким образом,
            значение итогового показателя по данной подшкале позволяет оценить не только уровень актуальной тревоги
            испытуемого, но и определить, находится ли он под воздействием стрессовой ситуации и какова интенсивность
            этого воздействия на него.
            <br/>
            <br/>
            • Личностная тревожность представляет собой конституциональную черту, обусловливающую склонность
            воспринимать достаточно широкий «веер» ситуаций как угрожающие, отвечая на каждую из них определенной
            реакцией. Как предрасположенность, личная тревожность активизируется при восприятии определенных стимулов,
            расцениваемых человеком как опасные для самооценки, самоуважения. При высокой личностной тревожности каждая
            из этих ситуаций будет обладать стрессовым воздействием на субъекта и вызывать у него выраженную тревогу.
            Очень высокая личностная тревожность прямо коррелирует с наличием невротического конфликта, с эмоциональными
            и невротическими срывами и психосоматическими заболеваниями.
        </p>
        <h2 class="mb-4">Содержательная интерпретация</h2>
        <p class="testCard testCard-point py-1 mb-4">
            • Ситуативная или реактивная тревожность как состояние характеризуется субъективно переживаемыми эмоциями:
            напряжением, беспокойством, озабоченностью, нервозностью. Это состояние отличается неустойчивостью во
            времени и различной интенсивностью в зависимости от силы воздействия стрессовой ситуации. Таким образом,
            значение итогового показателя по данной подшкале позволяет оценить не только уровень актуальной тревоги
            испытуемого, но и определить, находится ли он под воздействием стрессовой ситуации и какова интенсивность
            этого воздействия на него.
        </p>
    </div>
</template>

<script>

export default {
    name: "test-finale",
    components: {}
}
</script>