from django.shortcuts import get_object_or_404
from django.views import generic

from topics.models import (
    Topic,
    CurriculumArea,
    CurriculumIntegration,
    UnitPlan,
    ProgrammingExercise,
    ProgrammingExerciseLanguageImplementation,
    Lesson
)


class IndexView(generic.ListView):
    template_name = 'dev/index.html'
    context_object_name = 'all_topics'

    def get_queryset(self):
        """Return all topics"""
        return Topic.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Get topic, unit plan and lesson lists
        context['topics'] = Topic.objects.order_by('name')
        context['unit_plans'] = []

        # Build dictionaries for each unit plan and lesson
        for topic in context['topics']:
            topic.unit_plans = UnitPlan.objects.filter(topic=topic)
            for unit_plan in topic.unit_plans:
                unit_plan.lessons = unit_plan.lessons_by_age_group()
            context['unit_plans'] += topic.unit_plans

        # Get curriculum area clist
        context['curriculum_areas'] = CurriculumArea.objects.all()

        # Get curriculum integration list
        context['cur_int_activites'] = CurriculumIntegration.objects.all()

        # Get programming exercise list
        context['programming_exercises'] = ProgrammingExercise.objects.all().order_by(
            'exercise_set_number', 'exercise_number'
        )

        return context

class ProgrammingExerciseView(generic.DetailView):
    model = ProgrammingExercise
    template_name = 'dev/programming_exercise.html'
    context_object_name = 'programming_exercise'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model.objects.select_related(),
            slug=self.kwargs.get('programming_exercise_slug', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProgrammingExerciseView, self).get_context_data(**kwargs)
        # Add all the connected learning outcomes
        context['programming_exercise_learning_outcomes'] = self.object.learning_outcomes.all()
        context['implementations'] = self.object.implementations.all().order_by('-language__name').select_related()
        print('context', context)
        return context

class ProgrammingExerciseLanguageSolutionView(generic.DetailView):
    model = ProgrammingExerciseLanguageImplementation
    template_name = 'dev/programming_exercise_language_solution.html'
    context_object_name = 'implementation'

    def get_object(self, **kwargs):
        return get_object_or_404(
            self.model.objects.select_related(),
            exercise__slug=self.kwargs.get('programming_exercise_slug', None),
            language__slug=self.kwargs.get('programming_language_slug', None)
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProgrammingExerciseLanguageSolutionView, self).get_context_data(**kwargs)
        context['programming_exercise'] = self.object.exercise
        return context
