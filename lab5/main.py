from digital_machine import *


if __name__ == "__main__":
    table, field_names = generate_transition_table()
    print("\nТаблица переходов автомата:")
    print(table)

    for t_signal in ['T2', 'T1', 'T0']:
        sdnf = create_sdnf_from_transitions(table, field_names, t_signal)
        merged_sdnf = merging(sdnf)
        print(f"\nСДНФ для {t_signal}:")
        print(format_str(sdnf))
        print(f'\n{format_str(merged_sdnf)}')
