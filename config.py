from auxiliar import mock_items, generate_config_table

load_capacity = 4000 #kg
individuals_number = 150
generations = 100
items = mock_items() #Instancia os itens disponíveis para serem carregados
items_number = len(items)

#Gera tabela com as informações de configurações para exibição na tela final
generate_config_table(load_capacity, individuals_number, generations)