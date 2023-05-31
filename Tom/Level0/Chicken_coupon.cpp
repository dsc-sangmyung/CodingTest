using namespace std;

int solution(int chicken) {
    int service = chicken % 10;
    chicken /= 10;

    int answer = 0;

    for (; chicken != 0; chicken /= 10) {
        answer += chicken;

        service += chicken % 10;
        if (service >= 10) {
            answer += service / 10;
            service = (service / 10) + (service % 10);
        }
    }
    return answer;
}
