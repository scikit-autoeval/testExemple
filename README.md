# 🧠 Contexto da tarefa
Imagine que você faz parte da equipe de ciência de dados de um banco digital que desenvolve modelos de machine learning para detecção de fraudes em transações financeiras.
O banco deseja verificar se o modelo treinado em 2024 continua confiável em 2025, já que houve uma mudança no comportamento das transações, fenômeno conhecido como data shift.

# 🔍 O que é Data Shift
Data shift ocorre quando a distribuição dos dados usados pelo modelo muda ao longo do tempo, tornando suas previsões menos confiáveis.

Essas mudanças podem acontecer, por exemplo, quando os usuários passam a utilizar novos métodos de pagamento, dispositivos diferentes ou horários alternativos de compra, o que faz com que o modelo treinado em dados antigos não reflita mais a realidade atual.

# ⚙️ O papel da biblioteca scikit-autoeval
A scikit-autoeval foi criada para lidar exatamente com esse tipo de problema.
Ela contém estimadores capazes de prever o comportamento e o desempenho de modelos supervisionados quando ocorre data shift, sem necessidade de acesso aos rótulos verdadeiros.
No seu caso, você deverá utilizar o estimador SHAP (ShapEvaluator), que emprega explicações baseadas em SHAP values para estimar o impacto do data shift nas métricas de desempenho (ex.: accuracy e F1-score).

# 🧾 Descrição dos dados
Os datasets fornecidos são:
fraude-2024-controle.csv: conjunto rotulado de treino e controle.
fraude-2025-controle.csv: conjunto de teste, sem rótulos disponíveis (cenário de predição futura).

# 🧪 Tarefa
Utilize o código fornecido e complete o trecho indicado, configurando corretamente o estimador SHAP da biblioteca scikit-autoeval para estimar o desempenho do modelo em 2025. Para isso, utilize a [documentação da biblioteca](https://scikit-autoeval.github.io/scikit-autoeval/index.html).