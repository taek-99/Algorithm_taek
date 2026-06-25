def solution(today, terms, privacies):
    answer = []

    terms_dict = {t: int(month) for t, month in (term.split() for term in terms)}

    today_y, today_m, today_d = map(int, today.split("."))
    today_days = (today_y * 12 * 28) + (today_m * 28) + today_d

    for i, privacy in enumerate(privacies):
        date, term = privacy.split()

        y, m, d = map(int, date.split("."))

        expire_days = (
            y * 12 * 28
            + m * 28
            + d
            + terms_dict[term] * 28
            - 1
        )

        if expire_days < today_days:
            answer.append(i + 1)

    return answer
