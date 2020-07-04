import json
import logging

from django.http import JsonResponse
from django.views.generic import View

from tops.models import Score, Rank


class UploadView(View):
    def post(self, request):
        # 接受页面上传的数据
        json_str = request.body
        dict_data = json.loads(json_str)
        username = dict_data.get('username', '')
        score = dict_data.get('score', '')
        print(f"json_str==>{json_str}, username==>{username}, score==>{score}")
        if username and score:
            # 获取数据库的数据
            old_scor = Score.objects.filter(client=username).first()
            if old_scor:
                if old_scor.score != score:
                    old_scor.score = score
                    old_scor.save()
            else:
                Score.objects.create(client=username, score=score)
            # 排名表数据更新
            Rank.objects.all().delete()
            score_li = [score_obj.id for score_obj in Score.objects.all().order_by('-score')]
            n = 1
            for i in score_li:
                Rank.objects.create(c_id_id=i, rank=n)
                n = n + 1
            return JsonResponse({'status': 'sucess'})
        return JsonResponse({'status': 'error'})


class ShowView(View):
    def get(self, request):
        try:
            start = int(request.GET.get('start', '1'))
            end = int(request.GET.get('end', '20'))
            username = request.GET.get('username')
            assert username
        except Exception as e:
            logging.error(f"e==>{e}")
            return JsonResponse({'status': 'error'})
        uscore = Score.objects.filter(client=username).first()
        if uscore:
            uscore = {'ranking': uscore.rank.rank, 'client': uscore.client, 'score': uscore.score}
        else:
            uscore = {}
        context = {'data': [{'ranking': scor.rank.rank, 'client': scor.client, 'score': scor.score} for scor in
                            Score.objects.all().order_by('-score')[start - 1:end]]}
        context['data'].append(uscore)
        return JsonResponse({'status': 'ok', 'context': context})
